import { useUser } from "./hooks/useUser";
import Error401 from "./errors/Error401";
import AuthService from "./services/auth.service";

const PrivateRoute = ({ children }) => {
  const { setUser } = useUser();
  console.log("PrivateRoute");
  
  if (!AuthService.getUserFromToken()) {
    return <Error401 />
  }

  return children;
}

export default PrivateRoute;
