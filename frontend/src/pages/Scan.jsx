import React, { useState } from "react";
import API from "../api";

const Scan = () => {
  const [image, setImage] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleFileChange = (e) => {
    setImage(e.target.files[0]);
  };

  const handleUpload = async () => {
    if (!image) return alert("Please select an image");

    setLoading(true);

    try {
      const formData = new FormData();
      formData.append("image", image);

      const res = await API.post("/scan", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });

      setResult(res.data);
    } catch (err) {
      console.error(err);
      setResult({ score: 0, result: "Upload Failed" });
    }

    setLoading(false);
  };

  return (
    <div style={{ padding: 20 }}>
      <h2>Deepfake Scan</h2>

      <input type="file" accept="image/*" onChange={handleFileChange} />

      <br /><br />

      <button onClick={handleUpload} disabled={loading}>
        {loading ? "Scanning..." : "Upload & Scan"}
      </button>

      <br /><br />

      {result && (
        <div>
          <h3>Result:</h3>
          <p>Score: {result.score}</p>
          <p>Status: {result.result}</p>
        </div>
      )}
    </div>
  );
};

export default Scan;