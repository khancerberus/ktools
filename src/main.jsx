import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App.jsx';

import 'primereact/resources/themes/arya-orange/theme.css';
import 'primereact/resources/primereact.min.css';
import 'bootstrap/dist/css/bootstrap.min.css';

import './main.css';

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
)
