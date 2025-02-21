#!/bin/bash

echo "🚀 BUILD START"

# Ensure Python & pip are installed
python3.9 -m ensurepip --default-pip
python3.9 -m pip install --upgrade pip

# Install dependencies
python3.9 -m pip install -r requirements.txt

# Apply database migrations
python3.9 manage.py migrate

# Collect static files (ensures Vercel detects them)
python3.9 manage.py collectstatic --noinput --clear

echo "✅ BUILD COMPLETE"
