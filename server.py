
"""Flask web application for the Emotion Detector."""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    """Display the detector and handle submitted text."""
    result = None
    error = None

    if request.method == "POST":
        text_to_analyze = request.form.get("text_to_analyze", "")

        if not text_to_analyze.strip():
            error = "Please enter some text to analyze."
        else:
            result = emotion_detector(text_to_analyze)

            if result["dominant_emotion"] is None:
                error = (
                    "Emotion detection is currently unavailable. "
                    "Please try again later."
                )

    return render_template("index.html", result=result, error=error)


if __name__ == "__main__":
    app.run(debug=True)
