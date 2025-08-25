@echo off
cd /d C:\Scripts\blitz_auto
call .venv\Scripts\activate
python -m src.run_all
pause
