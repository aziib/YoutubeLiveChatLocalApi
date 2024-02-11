import pytchat
import time

chat = pytchat.create(video_id="4xDzrJKXOOY")
while chat.is_alive():
    print(chat.get().json())
    time.sleep(5)