import axios from "axios";

const API = axios.create({
  baseURL: "https://deepfake-detector-2-gwe8.onrender.com",
});

export default API;