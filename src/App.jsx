import { useEffect } from "react";
import { Route } from "react-router-dom";
import { Routes } from "react-router-dom";

import { useUser } from "@hooks/useUser";
import Home from "./Home";
import Login from "./Login";
import PrivateRoute from "./PrivateRoute";
import Dashboard from "./Dashboard";
import SideNav from "./SideNav";
import PokeAPI from "./pages/pokeapi/PokeAPI";
import { useLocation } from "react-router-dom";
import FuentePokeAPI from "./pages/pokeapi/FuentePokeAPi";

const App = () => {
  const { user } = useUser();

  const location = useLocation();

  useEffect(() => {
  }, []);

  const route = (path, element) => {
    return (
      <Route path={path} element={
        <PrivateRoute>
          {element}
        </PrivateRoute>
      } />
    )
  }

  return (
    <div>
      {/* <Navigator /> */}
      {user && location.pathname !== '/pokeapi/fuente' &&
        <SideNav />
      }

      <div
        className={location.pathname !== '/pokeapi/fuente' ? "body-pd" : ""}
        id="body"
      >
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/login" element={<Login />} />
          <Route path="/pokeapi/fuente" element={<FuentePokeAPI />} />

          {route("/dashboard", <Dashboard />)}
          {route("/pokeapi", <PokeAPI/>)}

          <Route path="*" element={<h1>Not Found</h1>} />
        </Routes>
      </div>

    </div>
  );
}

export default App;
