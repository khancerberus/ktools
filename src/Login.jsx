import { useSearchParams } from "react-router-dom";
import { useNavigate } from "react-router-dom";

import { useUser } from "@hooks/useUser";
import { useEffect } from "react";

const Login = () => {
  const [params] = useSearchParams();
  const { setTitle, login } = useUser();
  const navigate = useNavigate();

  useEffect(() => {
    setTitle("Login");

    const code = params.get("code");
    params.set("code", null);
    if (code) {
      login(code, () => {
        navigate("/dashboard");
      }, () => {
        navigate("/");
      });
    }
  }, []);

  return (
    <div className="m-5">
      <h1 className="text-center">Loading</h1>
    </div>
  )
}

export default Login;
