import os

MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://your_mongo_url")
DB_NAME = "deepfake_db"
UPLOAD_FOLDER = "uploads"