#!/bin/sh

# Create the database and run migrations
python manage.py makemigrations
python manage.py migrate

# Collect static files (if needed)
python manage.py collectstatic --noinput

# Run tests and capture the exit status
python manage.py test
TEST_STATUS=$?
if [ $TEST_STATUS -ne 0 ]; then
  echo "Tests Failed - System halt!"
  exit $TEST_STATUS
fi

# Start the Django server
exec python manage.py runserver 0.0.0.0:8000

# Start the server
exec "$@"