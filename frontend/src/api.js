import axios from "axios";

const API = axios.create({
  baseURL: "https://deepfake-detector-1-9su9.onrender.com",
});

export default API;