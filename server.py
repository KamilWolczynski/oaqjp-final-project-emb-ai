"""
Flask server for emotion detection using Watson NLP.
This module provides a web interface for analyzing text emotions.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def emotion_detector_web():
    """
    Analyze text emotions via web interface.
    
    Returns:
        str: Formatted emotion analysis or error message
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and get the response
    response = emotion_detector(text_to_analyze)

    # Check if dominant_emotion is None (error case)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    # Extract individual emotions and dominant emotion from response
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # Return formatted string as requested using f-string
    return (f"For the given statement, the system response is 'anger': {anger}, "
            f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and "
            f"'sadness': {sadness}. The dominant emotion is {dominant_emotion}.")


@app.route("/")
def render_index_page():
    """
    Render the main index page.
    
    Returns:
        str: Rendered HTML template
    """
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host="localhost", port=5000)
    