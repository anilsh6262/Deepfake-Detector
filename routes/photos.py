from flask import Blueprint, request, jsonify
from utils.db import db
import os
from werkzeug.utils import secure_filename

photos_bp = Blueprint("photos", __name__)

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@photos_bp.route("/upload", methods=["POST"])
def upload_photo():

    file = request.files["image"]

    name = request.form.get("name")

    description = request.form.get("description")

    filename = secure_filename(file.filename)

    filepath = os.path.join(UPLOAD_FOLDER, filename)

    file.save(filepath)

    photo_data = {
        "name": name,
        "description": description,
        "image": filepath
    }

    db.photos.insert_one(photo_data)

    return jsonify({
        "message": "Photo uploaded successfully"
    })


@photos_bp.route("/", methods=["GET"])
def get_photos():

    photos = list(db.photos.find({}, {"_id": 0}))

    return jsonify(photos)