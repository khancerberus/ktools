import { useEffect } from "react";
import { Route } from "react-router-dom";
import { Routes } from "react-router-dom";

import { useUser } from "@hooks/useUser";
import Home from "./Home";
import Login from "./Login";
import PrivateRoute from "./PrivateRoute";
import Dashboard from "./Dashboard";
import SideNav from "./SideNav";

const App = () => {
  const { user } = useUser();

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
      {user &&
        <SideNav />
      }

      <div className="body-pd" id="body">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/login" element={<Login />} />

          {route("/dashboard", <Dashboard />)}

          <Route path="*" element={<h1>Not Found</h1>} />
        </Routes>
      </div>

    </div>
  );
}

export default App;
