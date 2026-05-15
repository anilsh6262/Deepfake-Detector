import { useState, useEffect } from "react";
import API from "../api";

function Scan() {

  const [photos, setPhotos] = useState([]);
  const [selectedImagePath, setSelectedImagePath] = useState("");
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);

  useEffect(() => {
    loadPhotos();
  }, []);

  const loadPhotos = async () => {
    const res = await API.get("/photos");
    setPhotos(res.data);
  };

  const handleScan = async () => {

    if (!selectedImagePath || !file) {
      alert("Select both images");
      return;
    }

    const formData = new FormData();

    formData.append("image1_path", selectedImagePath); // FIX
    formData.append("image2", file);

    try {
      const res = await API.post("/scan", formData);
      setResult(res.data);
    } catch (err) {
      console.log(err);
      alert("Scan failed");
    }
  };

  return (
    <div style={{ padding: "20px" }}>

      <h2>Scan Duplicate Image</h2>

      <select onChange={(e) => setSelectedImagePath(e.target.value)}>
        <option value="">Select Original Image</option>

        {photos.map((p, i) => (
          <option key={i} value={p.image}>
            {p.name}
          </option>
        ))}
      </select>

      <br /><br />

      <input type="file" onChange={(e) => setFile(e.target.files[0])} />

      <br /><br />

      <button onClick={handleScan}>
        Scan
      </button>

      <br /><br />

      {result && (
        <div>
          <h3>{result.result}</h3>
          <p>Score: {result.score}</p>
        </div>
      )}

    </div>
  );
}

export default Scan;