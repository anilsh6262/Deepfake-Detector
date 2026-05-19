from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)

# Enable CORS (VERY IMPORTANT for Vercel frontend)
CORS(app)

# Upload folder setup
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# -----------------------------
# HOME ROUTE
# -----------------------------
@app.route('/')
def home():
    return "Backend Running Successfully"


# -----------------------------
# UPLOAD + SCAN (COMBINED FIX)
# -----------------------------
@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        print("UPLOAD API HIT")

        # Check file exists
        if 'file' not in request.files:
            return jsonify({
                "score": 0,
                "status": "No file received"
            }), 400

        file = request.files['file']

        # Check filename
        if file.filename == '':
            return jsonify({
                "score": 0,
                "status": "Empty filename"
            }), 400

        # Save file
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        print("File saved:", filepath)

        # -----------------------------
        # DUMMY AI RESULT (replace later with ML model)
        # -----------------------------
        score = 0.85

        if score > 0.6:
            status = "Fake Image Detected"
        else:
            status = "Real Image Detected"

        return jsonify({
            "filename": file.filename,
            "score": score,
            "status": status
        })

    except Exception as e:
        print("ERROR:", str(e))
        return jsonify({
            "score": 0,
            "status": "Upload Failed",
            "error": str(e)
        }), 500


# -----------------------------
# OPTIONAL: REMOVE SCAN (NOT NEEDED)
# -----------------------------
@app.route('/scan', methods=['POST'])
def scan_file():
    return jsonify({
        "message": "Use /upload instead"
    })


# -----------------------------
# RUN APP (Render compatible)
# -----------------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)