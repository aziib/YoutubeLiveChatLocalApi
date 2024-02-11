import pytchat
chat = pytchat.create(video_id="4xDzrJKXOOY")
while chat.is_alive():
    for c in chat.get().sync_items():
        print(f"{c.author.name} - {c.message}")