import { useEffect } from "react";
import { Button } from "primereact/button";

import { useUser } from "@hooks/useUser";

const Dashboard = () => {
  const { user, setTitle } = useUser();

  useEffect(() => {
    setTitle("Dashboard");
  }, []);

  return (
    <div className="container">
      <div className="row">
        <div className="col-12">
          <h4 className="text-center my-3 titulo">DASHBOARD</h4>
        </div>
      </div>

      <hr />

      <div className="row">
        <div className="col-sm-12 col-md-6 col-lg-4 col-xl-3">
          <div className="card my-1" style={{minHeight: "10rem"}} data-bs-theme="dark">
            <div className="card-header">
              <h5 className="card-title m-0 text-center">POKEAPI</h5>
            </div>
            <div className="card-body">
              <p className="card-text">This is the PokeAPI application.</p>
            </div>
            <div className="card-footer text-center">
              <Button label="Go to PokeAPI" onClick={() => window.location.href = "https://pokeapi.co/"} />
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Dashboard;
