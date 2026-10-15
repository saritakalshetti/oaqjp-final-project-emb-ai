# Emotion Detector — Final Project

## Project Overview

This repository contains the **Final Project** for the course **Developing AI Applications with Python and Flask** by IBM on Coursera (`oaqjp-final-project-emb-ai`).

The **Emotion Detector Final Project** is an AI-powered web application built using Python and Flask. It detects and analyzes emotions from textual statements using the IBM Watson NLP Emotion Prediction service (embedded workflow). The application computes scores for five basic emotions: **anger**, **disgust**, **fear**, **joy**, and **sadness**, and identifies the **dominant emotion** with the highest score.

---

## Features

- **Watson NLP Integration**: Connects to the IBM Watson NLP runtime service endpoint to perform emotion detection.
- **Emotion Scoring & Dominant Emotion**: Extracts individual scores for `anger`, `disgust`, `fear`, `joy`, and `sadness`, determining the `dominant_emotion`.
- **Reusable Package**: Encapsulates emotion detection logic inside the `EmotionDetection` package with clean imports.
- **Robust Error Handling**: Safely handles empty strings, whitespace, HTTP 400 Bad Request responses, network timeouts, and unavailable endpoints.
- **Flask Web Application**: Interactive web interface running on `0.0.0.0:5000` with the `/emotionDetector` GET endpoint.
- **Exact Coursera Formatting**: Returns the formatted response string and exact error message (`Invalid text! Please try again!`) expected by the grading rubric.
- **Repeatable Unit Testing**: Automated unit tests using Python's `unittest` framework covering all course rubric test statements and edge cases.
- **Static Code Analysis**: Fully compliant with PEP 8 standards, achieving a **10.00/10** score on Pylint.

---

## Technology Stack

- **Language**: Python 3.11
- **Web Framework**: Flask
- **HTTP Client**: Requests
- **NLP Service**: IBM Watson NLP (`emotion_aggregated-workflow_lang_en_stock`)
- **Testing Framework**: Python `unittest` (with `unittest.mock`)
- **Code Linter**: Pylint

---

## Directory Structure

```text
oaqjp-final-project-emb-ai/
│
├── EmotionDetection/
│   ├── __init__.py               # Package initializer exposing emotion_detector
│   └── emotion_detection.py      # Watson NLP API integration and emotion parsing
│
├── static/
│   └── mywebscript.js            # Asynchronous JavaScript client making GET requests
│
├── templates/
│   └── index.html                # Web interface template for the application
│
├── server.py                     # Flask web server and routing logic
├── test_emotion_detection.py     # Unit test suite for emotion detection logic
├── requirements.txt              # Project dependencies (Flask, requests, pylint)
├── README.md                     # Final Project documentation
└── .gitignore                    # Git ignore file for Python and runtime artifacts
```

---

## Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/saritakalshetti/oaqjp-final-project-emb-ai.git
   cd oaqjp-final-project-emb-ai
   ```

2. **Create and activate a virtual environment (optional but recommended)**:
   ```bash
   python -m venv venv
   # On Windows:
   .\venv\Scripts\activate
   # On Linux/macOS:
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

## Running the Application

To run the Flask server locally:

```bash
python server.py
```

The application starts on `http://127.0.0.1:5000` (host `0.0.0.0`, port `5000`).

Open your web browser and navigate to:
```text
http://127.0.0.1:5000/
```

Type a statement into the input box and click **Run Sentiment Analysis** (or **Analyze Emotion**) to view the predicted emotion breakdown and dominant emotion.

---

## API Endpoints

### 1. Home Page
- **Route**: `GET /`
- **Description**: Renders `templates/index.html`.

### 2. Emotion Detector Endpoint
- **Route**: `GET /emotionDetector?textToAnalyze=<your_text>`
- **Description**: Analyzes text and returns the formatted response.

#### Example Successful Response:
For the query `/emotionDetector?textToAnalyze=I%20am%20glad%20this%20happened`:
```text
For the given statement, the system response is 'anger': 0.02, 'disgust': 0.02, 'fear': 0.02, 'joy': 0.92 and 'sadness': 0.02. The dominant emotion is joy.
```

#### Expected Blank-Input / Error Behavior:
For blank inputs, whitespace, or invalid requests (`/emotionDetector` or `/emotionDetector?textToAnalyze=`):
```text
Invalid text! Please try again!
```

---

## Running Unit Tests

Run the test suite using Python's `unittest` runner:

```bash
python -m unittest -v test_emotion_detection
```

Or run the test file directly:

```bash
python test_emotion_detection.py
```

### Verified Test Cases:
1. `I am glad this happened` $\rightarrow$ Dominant emotion: `joy`
2. `I am really mad about this` $\rightarrow$ Dominant emotion: `anger`
3. `I feel disgusted just hearing about this` $\rightarrow$ Dominant emotion: `disgust`
4. `I am so sad about this` $\rightarrow$ Dominant emotion: `sadness`
5. `I am really afraid that this will happen` $\rightarrow$ Dominant emotion: `fear`
6. Empty string `""` $\rightarrow$ Returns `None` for `dominant_emotion`
7. HTTP 400 Bad Request simulation $\rightarrow$ Returns `None` for all emotions
8. Connection timeout simulation $\rightarrow$ Graceful fallback without crash
9. Malformed response simulation $\rightarrow$ Graceful fallback without crash

---

## Static Code Analysis (Pylint)

To verify PEP 8 compliance and code quality, run Pylint on the server and module:

```bash
python -m pylint server.py
python -m pylint EmotionDetection/emotion_detection.py
```

Both files achieve a **10.00/10** rating.

---

## Watson Service Connectivity & Troubleshooting

### Understanding Watson API Connectivity
- The Watson NLP Emotion Prediction endpoint (`https://sn-watson-emotion.labs.skills.network/...`) is an internal microservice hosted inside the **IBM Developer Skills Network Cloud environment**.
- When running from inside the IBM Skills Network Cloud IDE lab, the endpoint resolves directly and returns live IBM Watson model scores.
- When executing outside the IBM Skills Network environment (e.g. on a local personal computer or personal network), connections to `sn-watson-emotion.labs.skills.network` typically time out (`ConnectTimeoutError`) because the internal IBM lab network is protected behind firewalls.

### Note on Unit Tests vs. Live API
- The unit test suite (`test_emotion_detection.py`) uses mocked responses to guarantee repeatable, offline execution without depending on external network availability.
- To obtain live Watson API scores and take screenshots of live predictions (Questions 3, 5, 7, and 11), run the project within the IBM Skills Network lab terminal and web preview.

---

## Peer-Graded Final Project Submission Checklist

| Question | Requirement | Status |
|---|---|---|
| Q1 | Repository URL & README explicitly stating **Final Project** | Verified |
| Q2 | `EmotionDetection/emotion_detection.py` request & headers | Verified |
| Q3 | Terminal execution evidence for Watson emotion detector | Prepared |
| Q4 | Output formatting extracting emotions & dominant emotion | Verified |
| Q5 | Formatted response output verification | Verified |
| Q6 | GitHub link to `EmotionDetection/__init__.py` | Verified |
| Q7 | Terminal execution evidence importing package | Prepared |
| Q8 | `test_emotion_detection.py` matching course rubric | Verified |
| Q9 | Unit test execution passing with `OK` | Verified |
| Q10 | Flask `server.py` implementation with `/emotionDetector` | Verified |
| Q11 | Web interface deployed with emotion analysis result | Prepared |
| Q12 | HTTP 400 Bad Request error handling returning `None` | Verified |
| Q13 | `server.py` blank input returning `Invalid text! Please try again!` | Verified |
| Q14 | Web interface screenshot displaying `Invalid text! Please try again!` | Prepared |
| Q15 | Server endpoint error response verification | Verified |
| Q16 | Pylint static code analysis achieving 10/10 | Verified |
