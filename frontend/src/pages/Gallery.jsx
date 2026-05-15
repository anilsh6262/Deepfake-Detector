import { useEffect, useState } from "react";
import API from "../api";

function Gallery() {

  const [photos, setPhotos] = useState([]);

  useEffect(() => {
    fetchPhotos();
  }, []);

  const fetchPhotos = async () => {
    const res = await API.get("/photos");
    setPhotos(res.data);
  };

  return (
    <div style={{ padding: "20px" }}>
      <h2>Gallery</h2>

      <div style={{ display: "flex", flexWrap: "wrap", gap: "10px" }}>

        {photos.map((p, i) => (
          <div key={i} style={{ border: "1px solid gray", padding: "10px" }}>
            <img
              src={`http://127.0.0.1:5000/${p.image}`}
              width="150"
            />
            <p>{p.name}</p>
          </div>
        ))}

      </div>
    </div>
  );
}

export default Gallery;