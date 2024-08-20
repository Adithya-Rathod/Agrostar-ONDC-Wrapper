#!/bin/bash

# make it executable using chmod +x and then simply run this bash script

# stop mongod
stop_mongodb() {
    echo "Stopping MongoDB..."
    sudo service mongod stop
    if [ $? -eq 0 ]; then
        echo "MongoDB stopped successfully."
    else
        echo "Failed to stop MongoDB."
        # exit 1
    fi
}

# stop celery worker
stop_celery() {
    echo "Stopping Celery worker..."
    pkill -f "celery -A app.celery worker"
    if [ $? -eq 0 ]; then
        echo "Celery worker stopped successfully."
    else
        echo "Failed to stop Celery worker."
        # exit 1
    fi
}

# stop celery beat scheduler
stop_celery_beat() {
    echo "Stopping Celery beat scheduler..."
    pkill -f "celery -A app.celery beat"
    if [ $? -eq 0 ]; then
        echo "Celery beat scheduler stopped successfully."
    else
        echo "Failed to stop Celery beat scheduler."
        # exit 1
    fi
}

# stop flask app
stop_flask_app() {
    echo "Stopping Flask app..."
    pkill -f "python3 app.py"
    if [ $? -eq 0 ]; then
        echo "Flask app stopped successfully."
    else
        echo "Failed to stop Flask app."
        # exit 1
    fi
}

# Main script execution
stop_flask_app
stop_celery_beat
stop_celery
stop_mongodb

echo "All services stopped successfully!"
