# Youtube Live Chat Local Api
make your own local api and fetching from Youtube Live chat

## Description
this is for using my sillytavern ai live chat extension [https://github.com/aziib/Extension-LiveChat](https://github.com/aziib/Extension-LiveChat)

if you like my code and used it, please support me on ko-fi [https://ko-fi.com/megaaziib](https://ko-fi.com/megaaziib)

your support help me improved on this project.

☢ You will need to take full responsibility for your action ☢

## Requirements
Python: [https://www.python.org/downloads/](https://www.python.org/downloads/)

i'm using python 3.11, don't know if other version will work

make sure you tick check add to path when installing the python

Git: [https://git-scm.com/downloads](https://git-scm.com/downloads)

## Install Manually
1. Clone this repository
```git
git clone https://github.com/aziib/YoutubeLiveChatLocalApi
```
2. go to the folder and Setup virtual environment
```python
python -m venv venv
```
3. Activate virtual environment
```python
venv\Scripts\activate.bat
```
4. Install requirements
```python
pip install -r requirements.txt
```
5. Edit fetching.py using notepad or any text editor and change video_id on line 8 to your youtube video id and then save it
```python
    chat = pytchat.create(video_id="4xDzrJKXOOY") \\<--- change this to your youtube video link id, it's unique numbers & letters after https://www.youtube.com/watch?v=
```
6. Run fetch.bat, it will fetch the live comments and saved it as json file named chat_saved.json. do not close the bat, don't open the json file or deleted it until you want to end your stream. (only delete the chat_saved.json file if you want to start new live stream)
  
7. Run api.bat, it will create local api at port 5006 and then you can get the api calls by type http://127.0.0.1:5006/chat

## Install Automatically
1. run install.bat, wait until it finish and then close it
2. Edit fetching.py using notepad or any text editor and change video_id on line 8 to your youtube video id and then save it
```python
    chat = pytchat.create(video_id="4xDzrJKXOOY") \\<--- change this to your youtube video link id, it's unique numbers & letters after https://www.youtube.com/watch?v=
```
3. Run fetch.bat, it will fetch the live comments and saved it as json file named chat_saved.json. do not close the bat, don't open the json file or deleted it until you want to end your stream. (only delete the chat_saved.json file if you want to start new live stream)
  
4. Run api.bat, it will create local api at port 5006 and then you can get the api calls by type http://127.0.0.1:5006/chat
