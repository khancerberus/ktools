import { useEffect } from "react";
import { Navigate, useLocation } from "react-router-dom";

import { useUser } from "@hooks/useUser";

const Error401 = () => {
	const { setUser } = useUser();
  const { location } = useLocation();

	useEffect(() => {
		setUser(null);
	}, []);

	return <Navigate to="/" state={{from: location}} replace />;
};

export default Error401;
