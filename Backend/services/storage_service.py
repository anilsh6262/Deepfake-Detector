import os
from werkzeug.utils import secure_filename

# Folder where uploaded images will be stored
UPLOAD_FOLDER = "uploads"

# Create uploads folder automatically if not exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def save_image(file):
    """
    Save uploaded image to uploads folder
    """

    # Secure filename
    filename = secure_filename(file.filename)

    # Full path
    path = os.path.join(UPLOAD_FOLDER, filename)

    # Save file
    file.save(path)

    # Return saved path
    return path