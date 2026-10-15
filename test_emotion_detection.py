
import unittest
from unittest.mock import Mock, patch

from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_joy(self, mock_post):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "emotionPredictions": [{
                "emotion": {
                    "anger": 0.01,
                    "disgust": 0.01,
                    "fear": 0.02,
                    "joy": 0.95,
                    "sadness": 0.01
                }
            }]
        }
        mock_post.return_value = mock_response

        result = emotion_detector("I am happy")
        self.assertEqual(result["dominant_emotion"], "joy")
        self.assertEqual(result["joy"], 0.95)

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_sadness(self, mock_post):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "emotionPredictions": [{
                "emotion": {
                    "anger": 0.01,
                    "disgust": 0.01,
                    "fear": 0.02,
                    "joy": 0.01,
                    "sadness": 0.95
                }
            }]
        }
        mock_post.return_value = mock_response

        result = emotion_detector("I am sad")
        self.assertEqual(result["dominant_emotion"], "sadness")

    def test_blank_input(self):
        result = emotion_detector("")
        self.assertIsNone(result["dominant_emotion"])

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_bad_request(self, mock_post):
        mock_response = Mock()
        mock_response.status_code = 400
        mock_post.return_value = mock_response

        result = emotion_detector("invalid input")
        self.assertIsNone(result["dominant_emotion"])


if __name__ == "__main__":
    unittest.main()
