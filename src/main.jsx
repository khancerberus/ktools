import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter } from "react-router-dom";

import { UserContextProvider } from "@contexts/UserContext.jsx";
import { AxiosInterceptor } from "@utils/api.axios.js";
import App from "./App.jsx";

import "primereact/resources/themes/arya-orange/theme.css";
import "primereact/resources/primereact.min.css";
import "primeicons/primeicons.css";
import "bootstrap/dist/css/bootstrap.min.css";

import "@assets/css/main.css";

ReactDOM.createRoot(document.getElementById("root")).render(
	// <React.StrictMode>
	<BrowserRouter>
		<UserContextProvider>
			<AxiosInterceptor>
				<App />
			</AxiosInterceptor>
		</UserContextProvider>
	</BrowserRouter>
	// </React.StrictMode>,
);
