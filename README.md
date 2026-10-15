
# Emotion Detector

A Python Flask web application that detects emotions in text using the Watson NLP emotion detection service.

## Features

- Detects anger, disgust, fear, joy, and sadness.
- Identifies the dominant emotion.
- Provides a web interface using Flask.
- Handles blank input and service errors.
- Includes unit tests.

## Technologies

- Python
- Flask
- Requests
- Watson NLP Emotion Detection API
- unittest
- Pylint

## Run the application

Install the dependencies:

    python -m pip install requests flask pylint

Start the web application:

    python server.py

Open http://127.0.0.1:5000 in your browser.

## Run tests

    python -m unittest -v test_emotion_detection

## Static code analysis

    python -m pylint server.py
