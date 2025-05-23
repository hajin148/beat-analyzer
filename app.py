# app.py
from flask import Flask, request, jsonify
import librosa
import os

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    file = request.files['file']
    file.save('temp_audio.wav')

    y, sr = librosa.load('temp_audio.wav')
    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
    beat_times = librosa.frames_to_time(beat_frames, sr=sr)
    os.remove('temp_audio.wav')

    return jsonify({'beat_times_ms': [int(t * 1000) for t in beat_times]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
