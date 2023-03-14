#!/bin/bash

rm db.sqlite3
rm -rf ./backendapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations backendapi
python3 manage.py migrate backendapi
python3 manage.py loaddata users
python3 manage.py loaddata tokens
python3 manage.py loaddata profiles
python3 manage.py loaddata event_types
python3 manage.py loaddata venues
python3 manage.py loaddata favorites
python3 manage.py loaddata events
# python3 manage.py loaddata attendees


# Run this command to seed database:    chmod u+x ./seed_database.sh