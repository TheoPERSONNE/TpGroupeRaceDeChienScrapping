import React, { useRef, useEffect } from 'react';
import './Dragon.css';

const Dragon = () => {
  const cursorRef = useRef();

  useEffect(() => {
    const cursor = cursorRef.current;
    const trail = [];
    const maxTrail = 40;

    const onMouseMove = (e) => {
      const dot = document.createElement('div');
      dot.className = 'cyber-dot';
      dot.style.left = `${e.clientX}px`;
      dot.style.top = `${e.clientY}px`;
      cursor.appendChild(dot);
      trail.push(dot);

      if (trail.length > maxTrail) {
        const oldDot = trail.shift();
        cursor.removeChild(oldDot);
      }
    };

    window.addEventListener('mousemove', onMouseMove);

    return () => {
      window.removeEventListener('mousemove', onMouseMove);
    };
  }, []);

  return <div ref={cursorRef} className="cyber-trail"></div>;
};

export default Dragon;