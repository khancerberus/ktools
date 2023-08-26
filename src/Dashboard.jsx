import { useEffect } from "react";
import { Button } from "@prismane/core";

import { useUser } from "@hooks/useUser";
import { useNavigate } from "react-router-dom";

const Dashboard = () => {
  const { setTitle } = useUser();
  const navigate = useNavigate();

  useEffect(() => {
    setTitle("Dashboard");
  }, [setTitle]);

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
              <Button className="btn-ktools bg-gradient" variant="primary" onClick={() => navigate("/pokeapi")}>
                CONFIGURAR
              </Button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Dashboard;
