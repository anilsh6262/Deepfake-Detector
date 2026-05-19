from flask import Blueprint, request, jsonify
import os
import cv2
import numpy as np

scan_bp = Blueprint("scan_bp", __name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# -----------------------------
# Helper function (simple AI placeholder)
# -----------------------------
def analyze_image(image_path):
    img = cv2.imread(image_path)

    if img is None:
        return 0.0

    # Resize for consistency
    img = cv2.resize(img, (200, 200))

    # Fake "deepfake score logic" (placeholder)
    mean_intensity = np.mean(img)

    # Convert to probability-like score (0–1)
    score = mean_intensity / 255

    # Reverse logic so darker images = higher fake score (demo only)
    fake_score = round(float(1 - score), 4)

    return fake_score


# -----------------------------
# Scan Route
# -----------------------------
@scan_bp.route("/scan", methods=["POST"])
def scan():
    try:
        if "file" not in request.files:
            return jsonify({
                "score": 0,
                "result": "No file received"
            }), 400

        file = request.files["file"]

        if file.filename == "":
            return jsonify({
                "score": 0,
                "result": "Empty file"
            }), 400

        path = os.path.join("uploads", file.filename)
        file.save(path)

        # 🔥 TEMP WORKING SCORE (no AI yet)
        score = 0.85

        status = "Fake Image Detected" if score > 0.6 else "Real Image Detected"

        return jsonify({
            "filename": file.filename,
            "score": score,
            "status": status
        })

    except Exception as e:
        return jsonify({
            "score": 0,
            "status": "Upload Failed",
            "error": str(e)
        })