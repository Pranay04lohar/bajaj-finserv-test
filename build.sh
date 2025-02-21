#!/bin/bash

echo "🚀 BUILD START"

# Ensure the correct Python version is used
python3.9 -m pip install --upgrade pip
python3.9 -m pip install -r requirements.txt

# Apply migrations (if using a database)
python3.9 manage.py migrate

# Collect static files for Vercel
python3.9 manage.py collectstatic --noinput --clear

echo "✅ BUILD COMPLETE"
