#!/bin/bash

# Kill any existing Django instances
pkill -f "python manage.py runserver"

# Start multiple instances on different ports
PORT=8011 python manage.py runserver 0.0.0.0:8011 &
PORT=8012 python manage.py runserver 0.0.0.0:8012 &
PORT=8013 python manage.py runserver 0.0.0.0:8013 &
PORT=8014 python manage.py runserver 0.0.0.0:8014 &

echo "Started 4 Django instances on ports 8011-8014"

sleep 4

echo "Starting request loop (Ctrl+C to stop)..."
while true; do
    curl http://localhost/api/requests/
    sleep 0.25
done
