from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)

# Enable CORS
CORS(app)

# Upload folder setup
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# Home route
@app.route('/')
def home():
    return "Backend Running Successfully"


# Upload Route
@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        print("UPLOAD API HIT")

        # Check file
        if 'file' not in request.files:
            return jsonify({"error": "No file received"}), 400

        file = request.files['file']

        # Empty filename
        if file.filename == '':
            return jsonify({"error": "Empty filename"}), 400

        # Save file
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)

        file.save(filepath)

        print("File saved:", filepath)

        return jsonify({
            "message": "Upload successful",
            "filename": file.filename,
            "path": filepath
        })

    except Exception as e:
        print("ERROR:", str(e))
        return jsonify({"error": str(e)}), 500


# Deepfake Scan Route
@app.route('/scan', methods=['POST'])
def scan_file():
    try:
        if 'file' not in request.files:
            return jsonify({"error": "No file received"}), 400

        file = request.files['file']

        if file.filename == '':
            return jsonify({"error": "Empty filename"}), 400

        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)

        file.save(filepath)

        # Dummy prediction
        score = 95
        status = "Fake Image Detected"

        return jsonify({
            "filename": file.filename,
            "score": score,
            "status": status
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Run App
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)