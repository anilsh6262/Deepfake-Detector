from datetime import datetime

def create_user(name, email, picture=None):
    return {
        "name": name,
        "email": email,
        "picture": picture,
        "createdAt": datetime.utcnow()
    }