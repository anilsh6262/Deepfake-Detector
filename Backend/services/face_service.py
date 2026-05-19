import cv2
import numpy as np

def compare_faces(img1_path, img2_path):
    """
    Compare two images using simple OpenCV difference method
    Returns similarity score and result
    """

    img1 = cv2.imread(img1_path)
    img2 = cv2.imread(img2_path)

    # Safety check
    if img1 is None or img2 is None:
        return {
            "score": 0.0,
            "result": "Invalid image"
        }

    # Resize images to same size
    img1 = cv2.resize(img1, (200, 200))
    img2 = cv2.resize(img2, (200, 200))

    # Convert difference
    diff = cv2.absdiff(img1, img2)

    # Normalize score (0 to 1)
    score = 1 - (np.mean(diff) / 255)

    # Clamp score between 0 and 1
    score = max(0.0, min(1.0, score))

    return {
        "score": float(round(score, 4)),
        "result": "Match" if score > 0.6 else "Different"
    }