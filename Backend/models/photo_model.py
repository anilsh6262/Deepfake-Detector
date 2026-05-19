from datetime import datetime

def create_photo(user_id, name, description, image_path, embedding=None):
    return {
        "userId": user_id,
        "name": name,
        "description": description,
        "imagePath": image_path,
        "embedding": embedding,
        "createdAt": datetime.utcnow()
    }