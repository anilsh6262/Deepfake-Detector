from flask import request, jsonify
import os
import cv2
import numpy as np

UPLOAD_FOLDER = "uploads"

def compare_images(img1_path, img2_path):
    img1 = cv2.imread(img1_path)
    img2 = cv2.imread(img2_path)

    if img1 is None or img2 is None:
        return 0.0

    img1 = cv2.resize(img1, (200, 200))
    img2 = cv2.resize(img2, (200, 200))

    diff = cv2.absdiff(img1, img2)
    score = 1 - (np.mean(diff) / 255)

    return round(float(max(0, min(score, 1))), 4)


@scan_bp.route("/scan", methods=["POST"])
def scan():
    if "image" not in request.files:
        return jsonify({"score": 0, "result": "No Image Found"}), 400

    file = request.files["image"]
    path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(path)

    # If comparing with itself (demo mode)
    score = compare_images(path, path)

    result = "Match" if score > 0.6 else "Different"

    return jsonify({
        "score": score,
        "result": result
    })