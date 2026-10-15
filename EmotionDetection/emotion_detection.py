
import requests


def emotion_detector(text_to_analyze):
    """Detect emotions from text using the Watson NLP service."""

    empty_result = {
        "anger": None,
        "disgust": None,
        "fear": None,
        "joy": None,
        "sadness": None,
        "dominant_emotion": None
    }

    if not text_to_analyze or not text_to_analyze.strip():
        return empty_result

    url = (
        "https://sn-watson-emotion.labs.skills.network/"
        "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )

    headers = {
        "grpc-metadata-mm-model-id":
        "emotion_aggregated-workflow_lang_en_stock"
    }

    payload = {"raw_document": {"text": text_to_analyze}}

    try:
        response = requests.post(
            url, json=payload, headers=headers, timeout=5
        )

        if response.status_code == 400:
            return empty_result

        response.raise_for_status()
        result = response.json()
        emotions = result["emotionPredictions"][0]["emotion"]

        return {
            "anger": emotions["anger"],
            "disgust": emotions["disgust"],
            "fear": emotions["fear"],
            "joy": emotions["joy"],
            "sadness": emotions["sadness"],
            "dominant_emotion": max(emotions, key=emotions.get)
        }

    except (requests.exceptions.RequestException, KeyError,
            IndexError, TypeError, ValueError):
        return empty_result
