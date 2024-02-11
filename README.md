# Youtube Live Chat Local Api
make your own local api and fetching from Youtube Live chat

## Description
if you like my code and used it, please support me on ko-fi [https://ko-fi.com/megaaziib](https://ko-fi.com/megaaziib)

your support help me improved on this project.

☢ You will need to take full responsibility for your action ☢

## Install Manually
1. Setup virtual environment
```python
python -m venv venv
```
2. Activate virtual environment
```python
venv\Scripts\activate.bat
```
3. Install requirements
```python
pip install -r requirements.txt
```
4. Edit fetching.py using notepad or any text editor and change video_id on line 8 to your youtube video id and then save it
```python
    chat = pytchat.create(video_id="4xDzrJKXOOY") \\<--- change this to your youtube video link id, it's unique numbers & letters after https://www.youtube.com/watch?v=
```
5. Run fetch.bat, it will fetch the live comments and saved it as json file named chat_saved.json. do not close the bat, don't open the json file or deleted it until you want to end your stream. (only delete the chat_saved.json file if you want to start new live stream)
  
6. Run api.bat, it will create local api at port 5006 and then you can get the api calls by type http://127.0.0.1:5006/chat

## Install Automatically
1. run install.bat, wait until it finish and then close it
2. Edit fetching.py using notepad or any text editor and change video_id on line 8 to your youtube video id and then save it
```python
    chat = pytchat.create(video_id="4xDzrJKXOOY") \\<--- change this to your youtube video link id, it's unique numbers & letters after https://www.youtube.com/watch?v=
```
3. Run fetch.bat, it will fetch the live comments and saved it as json file named chat_saved.json. do not close the bat, don't open the json file or deleted it until you want to end your stream. (only delete the chat_saved.json file if you want to start new live stream)
  
4. Run api.bat, it will create local api at port 5006 and then you can get the api calls by type http://127.0.0.1:5006/chat
