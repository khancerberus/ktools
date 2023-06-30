import { createContext } from "react";
import AuthService from "../services/auth.service";
import { useState } from "react";
import { useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { useLocation } from "react-router-dom";

export const UserContext = createContext();

export const UserContextProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [title, setTitle] = useState(null);
  const navigate = useNavigate();
  const { location } = useLocation();

  const login = async (code, onSuccess, onFail) => {
    await AuthService.login(code).then(
      (data) => {
        setUser(AuthService.getUserFromToken());
        onSuccess(data);
      },
      (error) => {
        onFail(error);
      }
    );
  };

  const logout = () => {
    AuthService.logout();
    setUser(null);
    navigate("/", { replace: true, state: { from: location } });
  };



  useEffect(() => {
    const user = AuthService.getUserFromToken();
    setUser(user);
  }, []);

  return (
    <UserContext.Provider
      value={{
        user,
        setUser,
        login,
        logout,
        title,
        setTitle
      }}
    >
      {children}
    </UserContext.Provider>
  );
};
