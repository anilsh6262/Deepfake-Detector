import Upload from "./pages/Upload";
import Gallery from "./pages/Gallery";
import Scan from "./pages/Scan";

function App() {
  return (
    <div style={{ padding: "20px" }}>

      <h1>Deepfake Detector</h1>

      <Upload />
      <hr />
      <Gallery />
      <hr />
      <Scan />

    </div>
  );
}

export default App;