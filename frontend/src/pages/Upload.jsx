import { useState } from "react";
import API from "../api";

function Upload() {

  const [image, setImage] = useState(null);
  const [name, setName] = useState("");
  const [description, setDescription] = useState("");
  const [message, setMessage] = useState("");

  const handleUpload = async (e) => {

    e.preventDefault();

    if (!image) {
      alert("Please select an image");
      return;
    }

    const formData = new FormData();
    formData.append("image", image);
    formData.append("name", name);
    formData.append("description", description);

    try {

      const res = await API.post("/photos/upload", formData);

      setMessage(res.data.message);

    } catch (err) {
      console.log(err);
      setMessage("Upload failed");
    }
  };

  return (
    <div style={{ padding: "20px" }}>

      <h2>Upload Image</h2>

      <form onSubmit={handleUpload}>

        <input
          type="text"
          placeholder="Enter Name"
          value={name}
          onChange={(e) => setName(e.target.value)}
        />

        <br /><br />

        <textarea
          placeholder="Enter Description"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
        />

        <br /><br />

        <input
          type="file"
          accept="image/*"
          onChange={(e) => setImage(e.target.files[0])}
        />

        <br /><br />

        <button type="submit">
          Upload Image
        </button>

      </form>

      <p>{message}</p>

    </div>
  );
}

export default Upload;