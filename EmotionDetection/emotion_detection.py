"""
Emotion detection module using the IBM Watson NLP service.
"""
import requests


def emotion_detector(text_to_analyse):
    """
    Analyzes the provided text and returns emotion scores and the dominant emotion.

    Args:
        text_to_analyse (str): Text string to analyze for emotion.

    Returns:
        dict: Emotion scores (anger, disgust, fear, joy, sadness) and dominant_emotion.
    """
    empty_response = {
        'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None,
        'dominant_emotion': None
    }

    if not text_to_analyse or not str(text_to_analyse).strip():
        return empty_response

    url = (
        "https://sn-watson-emotion.labs.skills.network/"
        "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )

    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    payload = {
        "raw_document": {
            "text": text_to_analyse
        }
    }

    try:
        response = requests.post(
            url,
            json=payload,
            headers=headers,
            timeout=10
        )
    except requests.exceptions.RequestException:
        return empty_response

    if response.status_code == 400:
        return empty_response

    if response.status_code != 200:
        return empty_response

    data = response.json()
    emotions = data['emotionPredictions'][0]['emotion']

    scores = {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness']
    }

    dominant_emotion = max(scores, key=scores.get)
    scores['dominant_emotion'] = dominant_emotion

    return scores
