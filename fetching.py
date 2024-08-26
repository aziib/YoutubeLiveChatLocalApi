import pytchat
import json
import time
import os

# Create a function to fetch and save chat messages
def save_chat_messages():
    # Create pytchat instance with the desired video ID
    chat = pytchat.create(video_id="Gp4aaIzY5P0")
    
    # Check if 'chat_saved.json' exists and delete it if it does (only once at the start)
    if os.path.exists('chat_saved.json'):
        os.remove('chat_saved.json')
        print("Deleted existing chat_saved.json")

    while True:
        try:
            # Continuously fetch and store chat messages until the chat is alive
            while chat.is_alive():
                # Initialize an empty list to store chat messages for this iteration
                chat_messages = []

                # Fetch chat messages with retry mechanism
                while True:
                    try:
                        for c in chat.get().sync_items():
                            # Check if the message contains the keyword "!c"
                            if "!c" in c.message:
                                # Remove "!c" from the message before saving
                                cleaned_message = c.message.replace("!c", "").strip()
                                
                                # Append chat message details to the list
                                chat_messages.append({
                                    "author": c.author.name,
                                    "message": cleaned_message
                                })
                        break
                    except Exception as fetch_error:
                        print(f"Error fetching chat messages: {fetch_error}. Retrying in 1 second...")
                        time.sleep(1)

                # Load existing chat messages from JSON file if it exists
                try:
                    with open('chat_saved.json', 'r') as json_file:
                        existing_chat_messages = json.load(json_file)
                except FileNotFoundError:
                    existing_chat_messages = []

                # Combine existing messages with new ones
                all_chat_messages = existing_chat_messages + chat_messages

                # Save all chat messages to JSON file
                try:
                    with open('chat_saved.json', 'w') as json_file:
                        json.dump(all_chat_messages, json_file, indent=4)
                    print("Chat messages saved to chat_saved.json")
                except Exception as save_error:
                    print(f"Error saving chat messages: {save_error}")

                # Sleep for 4 seconds
                time.sleep(4)

        except Exception as e:
            print(f"An error occurred: {e}. Restarting...")

# Call the function to start fetching and saving chat messages
save_chat_messages()
