import './App.css';
import Dashboard from "./pages/Dashboard/Dashboard.js";
import Navbar from './components/Navbar/Navbar';
import CreateBot from './pages/CreateBot/CreateBot';
import EditBot from "./pages/EditBot/EditBot";
import { Routes, Route } from "react-router-dom";

import 'bootstrap/dist/css/bootstrap.min.css';

function App() {
  return (
    <div className="App">
      <Navbar />
      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/create-bot" element={<CreateBot />} />
        <Route path="/bots/:botId/edit" element={<EditBot />} />
      </Routes>
    </div>
  );
}

export default App;
