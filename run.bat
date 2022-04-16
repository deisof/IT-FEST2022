@echo off

echo Check packs

pip3 install -r requirements.txt

echo Starting server

python main.py

TIMEOUT /T 5