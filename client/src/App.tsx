import { Routes, Route } from "react-router-dom";
import { HomePage } from "./components/HomePage";
import Login from "./components/Login";
function App() {
  return (
    <>
      <Routes>
        <Route path="/" element={<HomePage/>}/>
        <Route path="/login" element={<Login/>}/>
      </Routes>
    </>
  );
}

export default App;
