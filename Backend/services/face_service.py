from deepface import DeepFace

def compare_faces(img1_path, img2_path):

    try:
        result = DeepFace.verify(
            img1_path,
            img2_path,
            enforce_detection=False
        )

        print("DEBUG RESULT:", result)  # IMPORTANT

        distance = result["distance"]

        score = (1 - distance) * 100

        return {
            "result": "Duplicate" if score > 60 else "Original",
            "score": float(round(score, 2))
        }

    except Exception as e:
        print("ERROR:", str(e))
        return {
            "result": "Error",
            "score": 0,
            "error": str(e)
        }