// import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter } from "react-router-dom";

import { UserContextProvider } from "@contexts/UserContext.jsx";
import { AxiosInterceptor } from "@utils/api.axios.js";
import App from "./App.jsx";

import "primereact/resources/themes/arya-orange/theme.css";
import "primereact/resources/primereact.min.css";
import "primeicons/primeicons.css";
import "primeflex/primeflex.css";
import "bootstrap/dist/css/bootstrap.min.css";
import { PrismaneProvider } from "@prismane/core";
import { extendTheme } from "@prismane/core/themes";

import "@assets/css/main.css";

const theme = extendTheme({
	colors: {
		primary: {
			DEFAULT: "#7f0082",
			50: "#7f0082",
			100: "#d1004e",
			200: "#d1004e",
			300: "#d1004e",
			400: "#d1004e",
			500: "#d1004e",
			600: "#d1004e",
			700: "#d1004e",
			800: "#d1004e",
			900: "#d1004e",
		},
	}
})


ReactDOM.createRoot(document.getElementById("root")).render(
	// <React.StrictMode>
		<BrowserRouter>
			<UserContextProvider>
				<AxiosInterceptor>
					<PrismaneProvider theme={theme}>
						<App />
					</PrismaneProvider>
				</AxiosInterceptor>
			</UserContextProvider>
		</BrowserRouter>
	//</React.StrictMode>,
);
