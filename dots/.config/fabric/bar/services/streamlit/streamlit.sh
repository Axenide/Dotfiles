#!/bin/bash

# Check if the virtual environment exists, if not, create it
if [ ! -d "venv" ]; then
  python -m venv venv
fi

# Activate the virtual environment
source venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py --server.port 3141
