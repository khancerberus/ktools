import axios from "axios";
import { useUser } from "../hooks/useUser";
import { useEffect } from "react";
import { useState } from "react";

const apiAxios = axios.create({
  baseURL: 'http://localhost:5000/api'
});

export const AxiosInterceptor = ({ children }) => {
  const { logout } = useUser();
  const [isLoaded, setIsLoaded] = useState(false);

  useEffect(() => {
    apiAxios.interceptors.request.use(
      (config) => {
        const token = localStorage.getItem('access_token');
        if (token) {
          config.headers['Authorization'] = 'Bearer ' + token;
        }
        return config;
      },
      (error) => {
        Promise.reject(error);
      }
    );
    
    apiAxios.interceptors.response.use(
      (response) => {
        return response;
      },
      (error) => {
        if (error?.response?.status === 401) {
          logout();
        }
        return Promise.reject(error);
      }
    );
    setIsLoaded(true);
  }, []);

  return isLoaded && children;
}

export default apiAxios;
