#!/bin/bash

# Run backend tests

cd backend
source venv/bin/activate
pytest tests/ -v --cov=app
