import React from 'react';
import './Home.css';

const Home = () => {
  return (
    <div className="home-container">
      <h1 className="home-title">Bienvenue sur le Scraper de Chiens 🐶</h1>
      <p className="home-description">Cliquez sur "Races" pour voir les races de chien extraites depuis le web.</p>
    </div>
  );
};

export default Home;