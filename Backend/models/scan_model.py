from datetime import datetime

def create_scan(user_id, reference_id, uploaded_path, result, confidence_score, deepfake_score=0):
    return {
        "userId": user_id,
        "referencePhotoId": reference_id,
        "uploadedImagePath": uploaded_path,
        "result": result,  # "duplicate" or "original"
        "confidenceScore": confidence_score,
        "deepfakeScore": deepfake_score,
        "timestamp": datetime.utcnow()
    }