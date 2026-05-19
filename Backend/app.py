from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)

# ✅ Allow frontend (Vercel)
CORS(app, origins=[
    "https://deepfake-detector-ecru.vercel.app"
])

# -----------------------------
# Upload folder setup
# -----------------------------
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024  # 16MB limit


# -----------------------------
# Home route (test backend)
# -----------------------------
@app.route('/')
def home():
    return "Backend is running successfully"


# -----------------------------
# Upload API (MAIN FIX)
# -----------------------------
@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        print("UPLOAD HIT")

        # check file exists
        if 'file' not in request.files:
            return jsonify({"error": "No file sent"}), 400

        file = request.files['file']

        # check filename
        if file.filename == '':
            return jsonify({"error": "Empty filename"}), 400

        # save file
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(filepath)

        print("FILE SAVED:", filepath)

        # 🔥 TEMP SCORE (replace with AI model later)
        return jsonify({
            "message": "Upload success",
            "filename": file.filename,
            "score": 0.87
        }), 200

    except Exception as e:
        print("ERROR:", str(e))
        return jsonify({"error": str(e)}), 500


# -----------------------------
# Photos API (for gallery.jsx)
# -----------------------------
@app.route('/photos', methods=['GET'])
def photos():
    try:
        files = os.listdir(UPLOAD_FOLDER)

        data = []
        for f in files:
            data.append({
                "name": f,
                "image": f"uploads/{f}"
            })

        return jsonify(data)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# -----------------------------
# Run locally
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)