@echo off
rem Basic install script for ReconSync

python -m venv .venv
call .venv\Scripts\activate.bat
pip install -r requirements.txt

echo Virtual environment ready.