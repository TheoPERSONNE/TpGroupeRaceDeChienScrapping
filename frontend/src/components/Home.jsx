import React from 'react';
import './Home.css';
import Slider from './Slider';

const Home = () => {
  return (
    <div className="home-container">
      <h1 className="home-title">Bienvenue sur le Scraper de Chiens 🐶</h1>
      <p className="home-description">Cliquez sur "Races" pour voir les races de chien extraites depuis le web.</p>
      <Slider />
    </div>
  );
};

export default Home;