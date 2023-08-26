import { useUser } from "@/hooks/useUser";
import PokeAPIService from "@/services/pokeapi.service";
import { Button } from "primereact/button";
import { Fragment } from "react";
import { useEffect } from "react";
import { useState } from "react";
import { useSearchParams } from "react-router-dom";
import { Link } from "react-router-dom";

const PokeAPI = () => {
  const { user } = useUser();
  const [params, setParams] = useSearchParams();

  const [isSaving, setIsSaving] = useState(true);
  const [authorized, setAuthorized] = useState(false);
  const [authUrl, setAuthUrl] = useState(null);

  const Authorization = () => {
    return (
      <div className="">
        {authUrl ?
            <Link
              className="p-button p-button-primary link-underline link-underline-opacity-0 hover:link-underline-opacity-100"
              to={authUrl}
            >
              Autorizar PokeAPI
            </Link>
          :
            <Button
              className="p-button p-button-primary"
              label="Obteniendo url..."
              icon="pi pi-spin pi-spinner"
              disabled
            />
        }
      </div>
    )
  }

  const getConfig = () => {
    PokeAPIService.getConfig().then((data) => {
      console.log(data);
    });
  }

  useEffect(() => {
    if (params.get("code")) {
      PokeAPIService.saveAuthCode(params.get("code")).then((data) => {
        setAuthorized(data?.is_authorized);
        if (!data?.is_authorized) {
          setParams({});
          PokeAPIService.getAuthUrl().then((data) => {
            setAuthUrl(data?.url);
          });
          setIsSaving(false);
        } else {
          // TODO GET CONFIG FROM API
        }
      });
    } else {
      setIsSaving(false);

      PokeAPIService.isAuthorized().then((data) => {
        setAuthorized(data?.is_authorized);
        if (!data?.is_authorized) {
          PokeAPIService.getAuthUrl().then((data) => {
            setAuthUrl(data?.url);
          });
          console.log(data)
        } else {
          // TODO GET CONFIG FROM API
        }
      });
    }
  }, []);

  return (
    <Fragment>
      {isSaving ?
          <div className="flex flex-column">
            <div className="text-center w-100">
              <h2>Loading... <i className="pi pi-spin pi-spinner fs-2" /></h2>
            </div>
          </div>
        :
          <div className="flex flex-column">
            <div className="text-center w-100">
              <h1>PokeAPI</h1>
            </div>
      
            {authorized ?
                <div className="text-center">
                  <h2>Ya autorizaste PokeAPI</h2>
                </div>
              :
                <Authorization />
            }
          </div>
      }
    </Fragment>
  )
}

export default PokeAPI;
