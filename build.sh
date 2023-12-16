#!/bin/bash

# Build the project
echo "Building the project..."
pip install -r requirements.txt

echo "Make Migration..."
python3.10.12 manage.py makemigrations --noinput
python3.10.12 manage.py migrate --noinput

echo "Collect Static..."
python3.10.12 manage.py collectstatic --noinput --clear
