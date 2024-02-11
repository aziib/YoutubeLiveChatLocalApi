@echo off 
python -m venv venv
call timeout /t 3 [/nobreak]
call venv\Scripts\activate.bat
pip install -r requirements.txt
pause