import React, { useState } from "react";
import API from "../api";

const Scan = () => {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  // File select
  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  // Upload + Scan
  const handleScan = async () => {
    if (!file) {
      alert("Please select an image first");
      return;
    }

    setLoading(true);

    try {
      const formData = new FormData();
      formData.append("image", file); // MUST match backend key

      const res = await API.post("/scan", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });

      console.log("API RESPONSE:", res.data);

      setResult({
        score: res.data.score,
        result: res.data.result,
      });
    } catch (error) {
      console.error("Upload Error:", error);

      setResult({
        score: 0,
        result: "Upload Failed",
      });
    }

    setLoading(false);
  };

  return (
    <div style={{ padding: "20px" }}>
      <h2>Deepfake Scan</h2>

      {/* File Input */}
      <input type="file" accept="image/*" onChange={handleFileChange} />

      <br /><br />

      {/* Button */}
      <button onClick={handleScan} disabled={loading}>
        {loading ? "Scanning..." : "Upload & Scan"}
      </button>

      <br /><br />

      {/* Result */}
      {result && (
        <div>
          <h3>Result</h3>
          <p>Score: {result.score}</p>
          <p>Status: {result.result}</p>
        </div>
      )}
    </div>
  );
};

export default Scan;