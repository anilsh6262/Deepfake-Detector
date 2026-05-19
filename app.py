from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)

# allow frontend (Vercel)
CORS(app)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def home():
    return "Backend Running Successfully"


# -------------------------
# MAIN UPLOAD ROUTE (ONLY ONE YOU NEED)
# -------------------------
@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        print("UPLOAD API HIT")

        if 'file' not in request.files:
            return jsonify({
                "score": 0,
                "status": "No file received"
            }), 400

        file = request.files['file']

        if file.filename == '':
            return jsonify({
                "score": 0,
                "status": "Empty filename"
            }), 400

        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        print("File saved:", filepath)

        # -------------------------
        # TEMP AI LOGIC
        # -------------------------
        score = 0.85
        status = "Fake Image Detected"

        return jsonify({
            "filename": file.filename,
            "score": score,
            "status": status
        })

    except Exception as e:
        print("ERROR:", str(e))
        return jsonify({
            "score": 0,
            "status": "Upload Failed"
        }), 500


# REMOVE CONFUSION ROUTE (OPTIONAL SAFE)
@app.route('/scan', methods=['POST'])
def scan():
    return jsonify({
        "message": "Use /upload instead"
    })


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)