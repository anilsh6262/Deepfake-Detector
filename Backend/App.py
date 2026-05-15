from flask import Flask
from flask_cors import CORS

from routes.photos import photos_bp
from routes.scan import scan_bp

app = Flask(__name__)

CORS(app)

app.register_blueprint(photos_bp, url_prefix="/photos")
app.register_blueprint(scan_bp, url_prefix="/scan")

@app.route("/")
def home():
    return {"message": "Backend Running"}

if __name__ == "__main__":
    app.run(debug=True)