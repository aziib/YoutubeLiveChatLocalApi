import pytchat
import json
import time

# Create a function to fetch and save chat messages
def save_chat_messages():
    # Create pytchat instance with the desired video ID
    chat = pytchat.create(video_id="aOu7othJASo")

    while True:
        try:
            # Continuously fetch and store chat messages until the chat is alive
            while chat.is_alive():
                # Initialize an empty list to store chat messages for this iteration
                chat_messages = []

                for c in chat.get().sync_items():
                    # Append chat message details to the list
                    chat_messages.append({
                        "author": c.author.name,
                        "message": c.message
                    })

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

                # Sleep for 3 seconds
                time.sleep(3)

        except Exception as e:
            print(f"An error occurred: {e}. Restarting...")

# Call the function to start fetching and saving chat messages
save_chat_messages()
