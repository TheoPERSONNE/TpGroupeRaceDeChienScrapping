import React, { useEffect, useRef } from 'react';
import './EmojiCloud.css';

const emojis = ["🎉", "🐶", "✨", "🎈", "🐕"];

const EmojiCloud = () => {
  const containerRef = useRef();

  useEffect(() => {
    const container = containerRef.current;

    const spawnEmoji = () => {
      const emoji = document.createElement('div');
      emoji.className = 'emoji-floating';
      emoji.innerText = emojis[Math.floor(Math.random() * emojis.length)];
      emoji.style.left = `${Math.random() * 100}%`;
      emoji.style.animationDuration = `${4 + Math.random() * 4}s`;
      container.appendChild(emoji);

      setTimeout(() => {
        emoji.remove();
      }, 9000);
    };

    const interval = setInterval(spawnEmoji, 200);
    return () => clearInterval(interval);
  }, []);

  return <div ref={containerRef} className="emoji-cloud"></div>;
};

export default EmojiCloud;
