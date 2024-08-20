#!/bin/bash

# make it executable using chmod +x and then simply run this bash script

# for mongod
start_mongodb() {
    echo "Starting MongoDB..."
    sudo service mongod start
    if [ $? -eq 0 ]; then
        echo "MongoDB started successfully."
    else
        echo "Failed to start MongoDB."
        exit 1
    fi
}

# celery worker
start_celery() {
    echo "Starting Ce wleryorker..."
    celery -A scripts.celery_tasks worker --loglevel=info &
    if [ $? -eq 0 ]; then
        echo "Celery worker started successfully."
    else
        echo "Failed to start Celery worker."
        exit 1
    fi
}

# celery beat scheduler
start_celery_beat() {
    echo "Starting Celery beat scheduler..."
    celery -A scripts.celery_tasks beat --loglevel=info &
    if [ $? -eq 0 ]; then
        echo "Celery beat scheduler started successfully."
    else
        echo "Failed to start Celery beat scheduler."
        exit 1
    fi
}


start_flask_app() {
    echo "Starting Flask app..."
    python3 app.py
    if [ $? -eq 0 ]; then
        echo "Flask app started successfully."
    else
        echo "Failed to start Flask app."
        exit 1
    fi
}

# Main script execution
start_mongodb
start_celery
start_celery_beat
start_flask_app

echo "All services started successfully!"
