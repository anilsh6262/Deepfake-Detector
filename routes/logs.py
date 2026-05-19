from flask import Blueprint, jsonify

logs_bp = Blueprint("logs", __name__)

@logs_bp.route("/", methods=["GET"])
def get_logs():
    return jsonify([
        {
            "result": "Duplicate",
            "score": 89,
            "timestamp": "2026-05-19 10:30"
        },
        {
            "result": "Original",
            "score": 23,
            "timestamp": "2026-05-19 11:00"
        }
    ])