import React from 'react';
import './Home.css';
import Slider from './Slider';
import Dragon from './Dragon';
import EmojiCloud from './EmojiCloud';


const Home = () => {
  return (
    <div className="home-container">
      <EmojiCloud />
      <h1 className="home-title">Bienvenue sur le Scraper de Chiens 🐶</h1>
      <p className="home-description">Cliquez sur "Races" pour voir les races de chien extraites depuis le web.</p>
      <Slider />
      <Dragon />
    </div>
  );
};

export default Home;