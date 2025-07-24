import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import Home from './components/Home';
import Chien from './components/Chien';
import './App.css';

function App() {
  return (
    <Router>
      <nav className="navbar">
        <ul className="nav-list">
          <li><Link to="/">Accueil</Link></li>
          <li><Link to="/races">Races</Link></li>
        </ul>
      </nav>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/races" element={<Chien />} />
      </Routes>
    </Router>
  );
}

export default App;