from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)

# ✅ Strong CORS fix for Vercel frontend
CORS(app, resources={r"/*": {"origins": "*"}})

# ✅ Render-safe upload folder (IMPORTANT)
UPLOAD_FOLDER = "/tmp/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# Home route
@app.route('/')
def home():
    return "Backend Running Successfully"


# Upload + Predict Route (ONLY ONE NEEDED)
@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        print("UPLOAD API HIT")

        # Check file exists
        if 'file' not in request.files:
            return jsonify({"error": "No file received"}), 400

        file = request.files['file']

        if file.filename == '':
            return jsonify({"error": "Empty filename"}), 400

        # Save file
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        print("File saved:", filepath)

        # 🔥 Dummy prediction (replace with ML model later)
        score = 95
        status = "Fake Image Detected"

        return jsonify({
            "message": "Upload successful",
            "filename": file.filename,
            "score": score,
            "status": status
        })

    except Exception as e:
        print("ERROR:", str(e))
        return jsonify({"error": str(e)}), 500


# ✅ Run on Render (IMPORTANT FIX)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)