import React, { useState } from 'react';
import './Chien.css';
import Dragon from './Dragon';
import EmojiCloud from './EmojiCloud';
import RaceDetail from './RaceDetails';
import RacesList from './RacesList';

const Chien = () => {
  const [formData, setFormData] = useState({
    taille: '',
    activite: '',
    habitation: '',
    experience: '',
    enfants: '',
    allergies: ''
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = (e) => {
      e.preventDefault();
    console.log('Formulaire soumis :', formData);
    alert("Formulaire envoyé (non relié au backend)");
  };

  return (
      <div className='principal-container'>

    <div className="breeds-container">
      <h2 className="breeds-title">Races de chiens</h2>

      <form className="dog-form" onSubmit={handleSubmit}>
        <label>
          Taille du chien :
          <select name="taille" onChange={handleChange} required>
            <option value="">-- Choisir --</option>
            <option value="petit">Petit</option>
            <option value="moyen">Moyen</option>
            <option value="grand">Grand</option>
          </select>
        </label>

        <label>
          Niveau d’activité :
          <select name="activite" onChange={handleChange} required>
            <option value="">-- Choisir --</option>
            <option value="calme">Calme</option>
            <option value="modere">Modéré</option>
            <option value="sportif">Sportif</option>
          </select>
        </label>

        <label>
          Type d’habitation :
          <select name="habitation" onChange={handleChange} required>
            <option value="">-- Choisir --</option>
            <option value="appartement">Appartement</option>
            <option value="maison">Maison avec jardin</option>
          </select>
        </label>

        <label>
          Expérience avec les chiens :
          <select name="experience" onChange={handleChange} required>
            <option value="">-- Choisir --</option>
            <option value="debutant">Débutant</option>
            <option value="confirme">Confirmé</option>
          </select>
        </label>

        <label>
          Enfants à la maison :
          <select name="enfants" onChange={handleChange} required>
            <option value="">-- Choisir --</option>
            <option value="oui">Oui</option>
            <option value="non">Non</option>
          </select>
        </label>

        <label>
          Allergies :
          <select name="allergies" onChange={handleChange} required>
            <option value="">-- Choisir --</option>
            <option value="oui">Oui</option>
            <option value="non">Non</option>
          </select>
        </label>

        <button type="submit" className="submit-button">Envoyer</button>
      </form>

    </div>
    <div>
        <h1>Element du Scrap</h1>
        <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Voluptatem magni nam 
            consequuntur voluptatum officia, odio adipisci repudiandae, fugit suscipit impedit 
            amet maiores reprehenderit odit consectetur animi aliquid ut perferendis 
            corrupti?</p>
            <RacesList />
    </div>
    <Dragon />
    </div>
  );
};

export default Chien;