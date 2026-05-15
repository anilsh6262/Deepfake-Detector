from flask import Blueprint, request, jsonify
from services.face_service import compare_faces

scan_bp = Blueprint("scan", __name__)

@scan_bp.route("/", methods=["POST"])
def scan():

    image1_path = request.form.get("image1_path")
    image2 = request.files.get("image2")

    if not image1_path or not image2:
        return jsonify({"error": "Missing images"}), 400

    temp_path = "temp.jpg"
    image2.save(temp_path)

    result = compare_faces(image1_path, temp_path)

    return jsonify(result)