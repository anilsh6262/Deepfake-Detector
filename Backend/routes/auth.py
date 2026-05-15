from flask import Blueprint, request, jsonify

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    return jsonify({
        "message": "Logged in",
        "user": {
            "name": data.get("name"),
            "email": data.get("email")
        }
    })