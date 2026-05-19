import axios from "axios";

const API = axios.create({
  baseURL: "https://deepfake-detector-1-9su9.onrender.com",
  headers: {
    "Content-Type": "application/json",
  },
});

export default API;