import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import reportWebVitals from "./reportWebVitals";
import "bootstrap/dist/css/bootstrap.css";

import "./index.css";
import "./components/login.css";
import "./components/chat.css";
import LoginScreen from "./screens/loginScreen";
import ChatScreen from "./screens/chatScreen";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <Router>
    <Routes>
      <Route path={"/"} element={<LoginScreen />} />
      <Route path={"chat/:role/:username/:pw"} element={<ChatScreen />} />
    </Routes>
  </Router>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
