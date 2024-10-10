#!/bin/sh


echo "***Pre commit routine starting***"

echo "Step 1: Activating virtual environment..."
.venv\Scripts\activate

echo "Step 2: Freezing packages and depndencies in requirements.txt ..."
python3 -m pip freeze > requirements.txt

echo "Step 3: Running locally the tests..."
