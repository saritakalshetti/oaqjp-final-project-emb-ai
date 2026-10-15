"""
Unit tests for the Emotion Detection application.
Tests emotion detection statements from the course rubric as well as error handling.
"""
import unittest
from unittest.mock import patch, MagicMock
import requests
from EmotionDetection.emotion_detection import emotion_detector


def _mocked_requests_post(_url, *_args, **kwargs):
    """
    Helper function simulating the Watson NLP Emotion Predict service
    for repeatable, network-independent unit tests.
    """
    mock_resp = MagicMock()
    json_data = kwargs.get("json", {})
    text = ""
    if isinstance(json_data, dict):
        text = json_data.get("raw_document", {}).get("text", "")

    # Blank / whitespace input simulates Watson 400 Bad Request
    if not text or not str(text).strip():
        mock_resp.status_code = 400
        mock_resp.text = '{"code": 400, "message": "Bad Request"}'
        mock_resp.json.return_value = {"code": 400, "message": "Bad Request"}
        return mock_resp

    # Default baseline scores
    emotions = {
        "anger": 0.02,
        "disgust": 0.02,
        "fear": 0.02,
        "joy": 0.02,
        "sadness": 0.02
    }

    lower_text = str(text).lower()
    if "glad" in lower_text or "happy" in lower_text:
        emotions["joy"] = 0.92
    elif "mad" in lower_text or "angry" in lower_text:
        emotions["anger"] = 0.91
    elif "disgust" in lower_text:
        emotions["disgust"] = 0.90
    elif "sad" in lower_text:
        emotions["sadness"] = 0.89
    elif "afraid" in lower_text or "fear" in lower_text:
        emotions["fear"] = 0.88
    else:
        emotions["joy"] = 0.50

    mock_resp.status_code = 200
    mock_resp.json.return_value = {
        "emotionPredictions": [
            {
                "emotion": emotions
            }
        ]
    }
    return mock_resp


class TestEmotionDetector(unittest.TestCase):
    """
    Unit test class for the emotion_detector function.
    """

    @patch("requests.post", side_effect=_mocked_requests_post)
    def test_emotion_detector(self, _mock_post):
        """
        Tests the 5 core statements specified by the course rubric:
        1. 'I am glad this happened' -> joy
        2. 'I am really mad about this' -> anger
        3. 'I feel disgusted just hearing about this' -> disgust
        4. 'I am so sad about this' -> sadness
        5. 'I am really afraid that this will happen' -> fear
        """
        # Test case 1: Joy
        result_1 = emotion_detector("I am glad this happened")
        self.assertEqual(result_1["dominant_emotion"], "joy")

        # Test case 2: Anger
        result_2 = emotion_detector("I am really mad about this")
        self.assertEqual(result_2["dominant_emotion"], "anger")

        # Test case 3: Disgust
        result_3 = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result_3["dominant_emotion"], "disgust")

        # Test case 4: Sadness
        result_4 = emotion_detector("I am so sad about this")
        self.assertEqual(result_4["dominant_emotion"], "sadness")

        # Test case 5: Fear
        result_5 = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result_5["dominant_emotion"], "fear")

    @patch("requests.post", side_effect=_mocked_requests_post)
    def test_empty_input(self, _mock_post):
        """
        Tests that empty or whitespace input returns None for dominant_emotion.
        """
        result = emotion_detector("")
        self.assertIsNone(result["dominant_emotion"])

    @patch("requests.post")
    def test_http_400_response(self, mock_post):
        """
        Tests that an HTTP 400 response from the API returns None for all emotions.
        """
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_post.return_value = mock_response

        result = emotion_detector("invalid input")
        self.assertIsNone(result["dominant_emotion"])
        self.assertIsNone(result["anger"])

    @patch("requests.post", side_effect=requests.exceptions.ConnectTimeout)
    def test_connection_timeout(self, _mock_post):
        """
        Tests that connection timeouts are handled safely without crashing.
        """
        result = emotion_detector("I am glad this happened")
        self.assertIsNone(result["dominant_emotion"])

    @patch("requests.post")
    def test_malformed_response(self, mock_post):
        """
        Tests that malformed JSON responses are handled gracefully.
        """
        mock_response = MagicMock()
        mock_response.status_code = 500
        mock_post.return_value = mock_response

        result = emotion_detector("Test malformed")
        self.assertIsNone(result["dominant_emotion"])


if __name__ == "__main__":
    unittest.main()
