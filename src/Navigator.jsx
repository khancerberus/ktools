import { Button } from "primereact/button";
import { Sidebar } from "primereact/sidebar";
import { useState } from "react";
import { useUser } from "./hooks/useUser";
import { Fragment } from "react";
import { Avatar } from "primereact/avatar";
import { useNavigate } from "react-router-dom";

const Navigator = () => {
  const { user, logout, title } = useUser();
  const navigate = useNavigate();
  const [visible, setVisible] = useState(false);

  return (
    <nav className="navbar shadow">
      <div className="container-fluid">
        <h4 className="mx-3" onClick={() => navigate("/")}>KTOOLS</h4>
        <ul className="navbar-nav text-center">
          <li className="nav-item">
            <h5>{title}</h5>
          </li>
        </ul>

        <div>
          {user &&
            <Fragment>
              <Avatar
                image={user.profile_image_url}
                onClick={() => setVisible(true)}
              />
              <Sidebar visible={visible} onHide={() => setVisible(false)} position="right">
                <div className="container text-center">
                  <h3 className="mb-5">{user.username}</h3>
                  <Button
                    label="Cerrar sesion"
                    severity="danger"
                    onClick={() => logout()}
                  />
                </div>
              </Sidebar>
            </Fragment>
          }
        </div>
      </div>
    </nav>
  )
};

export default Navigator;
