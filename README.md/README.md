# Deepfake & Duplicate Image Detection System

AI-powered web application for detecting duplicate images and deepfake faces using facial recognition.

---

## Features

- Google OAuth Login
- Upload reference images
- Store images in MongoDB
- Duplicate image detection
- Deepfake detection
- Scan history logging
- Confidence score results
- React frontend
- Flask backend

---

## Tech Stack

### Frontend
- React
- Vite
- Axios

### Backend
- Flask
- Python
- face_recognition

### Database
- MongoDB Atlas

---

## Project Structure

```txt
deepfake-detector/
│
├── backend/
├── frontend/
└── README.md
```

---

## Backend Setup

### Install dependencies

```bash
cd backend

pip install -r requirements.txt
```

### Run backend

```bash
python app.py
```

Backend runs on:

```txt
http://localhost:5000
```

---

## Frontend Setup

### Install dependencies

```bash
cd frontend

npm install
```

### Run frontend

```bash
npm run dev
```

Frontend runs on:

```txt
http://localhost:5173
```

---

## APIs

### Upload Photo

```txt
POST /photos/upload
```

### Get Photos

```txt
GET /photos/
```

### Scan Duplicate

```txt
POST /scan/check
```

### Get Logs

```txt
GET /scan/logs
```

---

## Future Improvements

- Real Google OAuth
- CNN-based Deepfake Detection
- Cloudinary Storage
- Admin Dashboard
- Docker Deployment

---

## Author

Anil Hosamani