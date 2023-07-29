import { Button } from "primereact/button";
import { Fragment } from "react";
import { StyleClass } from "primereact/styleclass";
import { useNavigate } from "react-router-dom";
import { Avatar } from "primereact/avatar";
import { Dialog } from "primereact/dialog";

import "@assets/css/sidenav.css";
import { useRef } from "react";
import { useUser } from "./hooks/useUser";
import { useState } from "react";

const SideNav = () => {
  const { user, logout } = useUser();
  const navigate = useNavigate();
  const toggleButton = useRef(null);

  const [dialogVisible, setDialogVisible] = useState(false);

  const NavItem = ({ label, icon, path }) => (
    <li>
      <Button
        onClick={() => navigate(path)}
        className="w-100 my-1 rounded-0"
        size="large"
      >
        <i className={`pi ${icon}`}></i>
        <span className="ms-4">{label}</span>
      </Button>
    </li>
  )

  const userDialogHeader = () => (
    <div className="flex">
      <Avatar image={user.profile_image_url} size="xlarge" shape="circle" />
      <h3 className="flex ms-3 mt-2 align-items-center">{user.username}</h3>
    </div>
  )

  return (
    <Fragment>
      <StyleClass nodeRef={toggleButton} selector="#body" toggleClassName="body-pd" />

      <StyleClass nodeRef={toggleButton} selector=".header" toggleClassName="header-pd" />
      <header className="header shadow-4 header-pd" id="header">
        <div class="header_toggle">
          <Button
            className="header_toggle_button"
            ref={toggleButton}
            text
          >
            <i id="header-toggle" class="pi pi-bars text-white"></i>
          </Button>
        </div>

        <div className="flex">
          <Avatar
            image={user.profile_image_url}
            size="xlarge"
            shape="circle"
            onClick={() => setDialogVisible(true)}
          />

          <Dialog
            visible={dialogVisible}
            onHide={() => setDialogVisible(false)}
            modal={false}
            style={{minWidth: "40vw"}}
            header={userDialogHeader}
          >
            <div className="d-flex flex-column align-items-center">
              <Button
                label="Logout"
                className="w-100 my-2 bg-red-400 border-0"
                onClick={() => logout()}
              />
            </div>
          </Dialog>
        </div>
      </header>

      <StyleClass nodeRef={toggleButton} selector="#nav-bar" toggleClassName="show" />
      <div className="l-navbar show" id="nav-bar">
        <nav className="nav">
          <div>
            {/** LOGO */}

            <div class="nav_list">
              <ul className="list-group">
                <NavItem
                  label="Home"
                  icon="pi-home"
                  path="/"
                />

                <NavItem
                  label="Dashboard"
                  icon="pi-chart-bar"
                  path="/dashboard"
                />
              </ul>
            </div>
          </div>
        </nav>
      </div>
    </Fragment>
  )
};

export default SideNav;