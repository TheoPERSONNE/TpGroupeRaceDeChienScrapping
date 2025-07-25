import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import Home from './components/Home';
import Chien from './components/Chien';
import RaceDetails from './components/RaceDetails';
import RacesList from './components/RacesList';
import './App.css';


function App() {
  return (
    <Router>
      <nav className="navbar">
        <ul className="nav-list">
          <li><Link to="/">Accueil</Link></li>
          <li><Link to="/recommandation">Recommandation</Link></li>
          <li><Link to="/list">Liste</Link></li>
        </ul>
      </nav>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/recommandation" element={<RaceDetails />} />
        <Route path="/list" element={<RacesList />} />
      </Routes>
    </Router>
  );
}

export default App;