from flask import Flask, jsonify
from flask_cors import CORS
import os

from routes.photos import photos_bp
from routes.scan import scan_bp
from routes.logs import logs_bp

app = Flask(__name__)

CORS(app)

# ROUTES
app.register_blueprint(photos_bp, url_prefix="/photos")
app.register_blueprint(scan_bp, url_prefix="/scan")
app.register_blueprint(logs_bp, url_prefix="/logs")


@app.route("/")
def home():
    return jsonify({
        "message": "Backend Running"
    })


# DEPLOYMENT CONFIG
port = int(os.environ.get("PORT", 5000))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port)