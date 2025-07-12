import logo from './logo.svg';
import './App.css';
import React, { useState } from 'react'

function App() {
  const [caption, setCaption] = useState("");
  const [image, setImage] = useState(null);
  const [preview, setPreview] = useState(null);

  const handleSubmit = async(e) => {
    e.preventDefault();

    const formData = new FormData();
    formData.append("image", image);

    const res = await fetch("http://127.0.0.1:8000/caption/", {
      method: "POST",
      body: formData,
    });

    const data = await res.json();
    setCaption(data.caption || data.error);
  }

  const handleImageChange = async(e) => {
    const file = e.target.files[0];
    if (file) {
      setImage(file);
      setPreview(URL.createObjectURL(file));
    }
  };
  
  return (
    <div>
      <h1>Image Caption Generator</h1>
      <form onSubmit={handleSubmit}>
        <input type="file" accept="image/*" onChange={handleImageChange} />
        <button type="submit">Upload</button>
      </form>

      {preview && (
        <div style={{ marginTop: "20px" }}>
          <p>Preview:</p>
          <img src={preview} alt="Selected" style={{ maxWidth: "300px" }} />
        </div>
      )}

      <p>{caption}</p>
    </div>
  );
}

export default App;
