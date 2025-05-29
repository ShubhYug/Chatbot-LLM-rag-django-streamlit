#!/bin/bash

# Activate virtual environment
source env/bin/activate

# Run Django server in background
python manage.py runserver &

# Run Streamlit app in foreground
streamlit run streamlit_app.py