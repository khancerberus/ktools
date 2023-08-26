import { useState } from "react";
import { useRef } from "react";
import { useEffect } from "react";

import tmi from "tmi.js";

const FuentePokeAPI = () => {
  const socket = useRef(null);
  const [mensajes, setMensajes] = useState([]);

  useEffect(() => {
    document.body.style = 'background: transparent;';
    console.log('useEffect chat');
    socket.current = new tmi.Client({
      channels: ['khancerberus']
    });

    socket.current.connect();

    socket.current.on('message', (channel, tags, message) => {

      // Actualizar el estado solo con los últimos 5 mensajes
      const newMessage = `[${channel}] ${tags['display-name']}: ${message}`;
      setMensajes(prevMessages => {
        if (prevMessages.length >= 10) {
          return [...prevMessages.slice(1), newMessage];
        } else {
          return [...prevMessages, newMessage];
        }
      });
    });
  }, []);

  return (
    <div>
      <h1>WEBSOCKETS TWITCH</h1>
      <h2>CHAT</h2>

      <div className="text-white fs-1">
        <ul>
        {mensajes?.map((mensaje, index) => (
          <li key={index} className="text-white">{mensaje}</li>
        ))}
        </ul>
      </div>
    </div>
  )
}

export default FuentePokeAPI;
