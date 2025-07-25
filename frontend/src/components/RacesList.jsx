import React, { useState, useEffect } from "react";
import "./RacesList.css";

export default function RacesList() {
  const [races, setRaces] = useState([]);
  const [search, setSearch] = useState("");
  const [gabaritFilter, setGabaritFilter] = useState("");
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    async function fetchRaces() {
      setLoading(true);

      const params = new URLSearchParams();
      if (search.trim()) params.append("search", search.trim());
      if (gabaritFilter) params.append("gabarit", gabaritFilter);

      try {
        const res = await fetch(`http://localhost:8000/races?${params.toString()}`);
        if (!res.ok) throw new Error("Erreur API");
        const data = await res.json();
        setRaces(data.races || []);
      } catch (e) {
        alert("Erreur lors du chargement des races");
      } finally {
        setLoading(false);
      }
    }

    fetchRaces();
  }, [search, gabaritFilter]);

  const gabarits = Array.from(new Set(races.map((r) => r.gabarit))).filter(Boolean);

  return (
    <div className="races-list-container">
      <h2>Liste des races</h2>

      <div className="filters">
        <input
          type="text"
          placeholder="Rechercher par nom..."
          value={search}
          onChange={(e) => setSearch(e.target.value)}
        />

        <select
          value={gabaritFilter}
          onChange={(e) => setGabaritFilter(e.target.value)}
        >
          <option value="">Tous les gabarits</option>
          {gabarits.map((g) => (
            <option key={g} value={g}>
              {g}
            </option>
          ))}
        </select>
      </div>

      {loading ? (
        <p className="loading">Chargement...</p>
      ) : races.length === 0 ? (
        <p className="no-results">Aucune race trouvée.</p>
      ) : (
        <ul className="races-list">
          {races.map((race) => (
            <li key={race.nom} className="race-item">
              <h3>{race.nom}</h3>
              <p><b>Origine:</b> {race.origine}</p>
              <p><b>Gabarit:</b> {race.gabarit}</p>
              <p>{race.description || "Pas de description"}</p>
              <a href={race.url} target="_blank" rel="noreferrer">
                En savoir plus
              </a>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
