#!/bin/bash

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate

# Collect static files (if needed)
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Start the Django development server
echo "Starting server..."
python manage.py runserver 0.0.0.0:8000
