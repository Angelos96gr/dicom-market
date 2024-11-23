#!/bin/sh

echo "Activating venv"
.venv/Scripts/activate

echo "Installing dependencies"
pip install -r requirements.txt


echo "Starting server"
python backend/main.py start
