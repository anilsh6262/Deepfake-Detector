from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)

# -----------------------------
# CORS (Frontend allow)
# -----------------------------
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
# Home route (backend test)
# -----------------------------
@app.route('/')
def home():
    return "Backend is running successfully"


# -----------------------------
# Upload API
# -----------------------------
@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        print("UPLOAD HIT")

        # check file exists
        if 'file' not in request.files:
            return jsonify({"error": "No file sent"}), 400

        file = request.files['file']

        if file.filename == '':
            return jsonify({"error": "Empty filename"}), 400

        filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(filepath)

        print("FILE SAVED:", filepath)

        # 🔥 TEMP SCORE (replace with AI later)
        return jsonify({
            "message": "Upload success",
            "filename": file.filename,
            "score": 0.87
        }), 200

    except Exception as e:
        print("UPLOAD ERROR:", str(e))
        return jsonify({"error": str(e)}), 500


# -----------------------------
# Gallery API
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

        return jsonify(data), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# -----------------------------
# IMPORTANT: Render deployment fix
# -----------------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)