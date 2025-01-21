"""
Server for Emotion Detection Application.

This module provides an API endpoint to analyze emotions from a given text
using the Watson NLP Library.
"""

from flask import Flask, request, jsonify  # Removed unused render_template import
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_endpoint():
    """
    Endpoint to handle POST requests to detect emotions in the provided text.

    Processes the text and returns emotion scores and the dominant emotion.
    If the text is empty or invalid, an error message is returned.
    """
    # Extract the input statement
    data = request.get_json()
    text_to_analyze = data.get("text")

    if not text_to_analyze:
        return jsonify({"message": "Invalid text! Please try again!"}), 400

    # Process the text using the emotion detector
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return jsonify({"message": "Invalid text! Please try again!"}), 400

    # Format the output for the customer
    emotions = ", ".join([f"'{k}': {v}" for k, v in response.items() if k != 'dominant_emotion'])
    dominant_emotion = response['dominant_emotion']

    result = (
        f"For the given statement, the system response is {emotions}. "
        f"The dominant emotion is {dominant_emotion}."
    )

    return jsonify({"response": result})

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
