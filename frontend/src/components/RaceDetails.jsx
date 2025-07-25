import React, { useState } from "react";
import "./RaceDetails.css";
import EmojiCloud from "./EmojiCloud";


const SECTIONS = {
  activite: [
    "Sportif",
    "Niveau d'énergie",
    "Potentiel à jouer",
  ],
  caractere: [
    "Affectueux",
    "Calme",
    "Protecteur",
    "Indépendant",
    "Chasseur",
    "Aboie / Hurle",
  ],
  comportementautres: [
    "Cohabitation avec les enfants",
    "Sociable avec les autres animaux",
    "Aime les étrangers",
  ],
  conditionsvie: [
    "Adapté à la vie en appartement",
    "Bien pour les nouveaux maitres",
    "Aime le chaud",
    "Aime le froid",
  ],
  education: [
    "Intelligent",
    "Obéissant",
  ],
  entretien: [
    "Facilité d'entretien",
    "Coût de l'entretien",
    "Perte de poils",
  ],
  sante: [
    "Solide",
    "Facilité à prendre du poids",
  ],
  
};

export default function RaceDetails() {
  const [selectedSections, setSelectedSections] = useState([]);
  const [stats, setStats] = useState({});
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  // Gérer sélection/désélection des sections
  function toggleSection(section) {
    setStats((prev) => {
      const copy = { ...prev };
      if (!selectedSections.includes(section)) {
        // Init des stats pour cette section à 0
        copy[section] = SECTIONS[section].reduce((acc, key) => {
          acc[key] = 0;
          return acc;
        }, {});
      } else {
        delete copy[section];
      }
      return copy;
    });

    setSelectedSections((prev) =>
      prev.includes(section)
        ? prev.filter((s) => s !== section)
        : [...prev, section]
    );
  }

  function handleChange(section, key, value) {
    setStats((prev) => ({
      ...prev,
      [section]: {
        ...prev[section],
        [key]: Math.min(5, Math.max(0, Number(value) || 0)),
      },
    }));
  }
  const [modalOpen, setModalOpen] = useState(false);

  function openModal() {
    setModalOpen(true);
  }
  function closeModal() {
    setModalOpen(false);
  }
  async function handleSubmit(e) {
    e.preventDefault();
    setLoading(true);
    setResult(null);
    // Formate les données pour backend: chaque section est une liste d'un StatBlock
    const data = {};
    for (const section of selectedSections) {
      data[section] = [
        {
          resume: "",
          stats: stats[section],
        },
      ];
    }

    try {
      const res = await fetch("http://localhost:8000/recommandation", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data),
      });
      if (!res.ok) throw new Error("Erreur API");
      const json = await res.json();
     setResult(json.recommendations);
      openModal();
    } catch (e) {
      alert("Erreur lors de la requête");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="container">
      <h1 className="title">Recommandation de race de chien</h1>

      <div className="content">
        <aside className="sidebar">
          <h3>Choisissez les critères :</h3>
          {Object.keys(SECTIONS).map((section) => (
            <label key={section} className="checkbox-label">
              <input
                type="checkbox"
                checked={selectedSections.includes(section)}
                onChange={() => toggleSection(section)}
              />
              {section.charAt(0).toUpperCase() + section.slice(1)}
            </label>
          ))}
        </aside>

        <main className="main-form">
          <form onSubmit={handleSubmit}>
            {selectedSections.length === 0 && (
              <p className="info-text">Sélectionnez des critères pour afficher le formulaire.</p>
            )}

            {selectedSections.map((section) => (
              <div key={section} className="section-block">
                <h3>{section.charAt(0).toUpperCase() + section.slice(1)}</h3>
                {SECTIONS[section].map((key) => (
                  <div key={key} className="input-row">
                    <label>
                      {key} (0-5):
                      <input
                        type="number"
                        min={0}
                        max={5}
                        value={stats[section]?.[key] || 0}
                        onChange={(e) => handleChange(section, key, e.target.value)}
                        required
                      />
                    </label>
                  </div>
                ))}
              </div>
            ))}

            <button
              type="submit"
              disabled={loading || selectedSections.length === 0}
              className="submit-btn"
            >
              {loading ? "Chargement..." : "Trouver les races"}
            </button>
          </form>
        </main>
      </div>

      {modalOpen && (
        <div className="modal-overlay" onClick={closeModal}>
          <div
            className="modal-content"
            onClick={(e) => e.stopPropagation()} // empêche fermeture au clic dans la modal
          >
            <button className="modal-close" onClick={closeModal}>
              &times;
            </button>
          
            <h2>Résultats</h2>
            <EmojiCloud />
            {result && result.length === 0 && <p>Aucune race trouvée</p>}

            {result?.map((race, i) => (
              <div key={i} className="result-card">
                <h3>{race.nom}</h3>
                <p>{race.description || "Pas de description"}</p>
                <p><b>Origine:</b> {race.origine}</p>
                <p><b>Gabarit:</b> {race.gabarit}</p>
                <a href={race.url} target="_blank" rel="noreferrer" className="link-btn">
                  En savoir plus
                </a>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}
