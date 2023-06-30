import { Button } from "primereact/button";
import { useNavigate } from "react-router-dom";
import { useUser } from "./hooks/useUser";
import { useEffect } from "react";

const TWITCH_CLIENT_ID = import.meta.env.VITE_TWITCH_CLIENT_ID;

const Home = () => {
  const { user, setTitle } = useUser();
  const navigate = useNavigate();

  useEffect(() => {
    setTitle("");

  }, []);

  return (
    <div className="m-5">
      <Button
        label={user ? "Go to dashboard" : "Click to login"}
        onClick={() => {
          user ?
              navigate("/dashboard")
            :
              window.location.href = "https://id.twitch.tv/oauth2/authorize?client_id=" + TWITCH_CLIENT_ID + "&redirect_uri=http://localhost:5173/login&response_type=code&scope=user:read:email";
        }}
      />
    </div>
  )
}

export default Home;
