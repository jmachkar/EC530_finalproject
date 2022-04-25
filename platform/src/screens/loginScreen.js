import React, { Component } from "react";
import "../components/login.css";
import Buttons from "../components/buttons";
import Login from "../components/loginBox";

class LoginScreen extends Component {
  state = {};
  render() {
    return (
      <div className="main">
        <Buttons />
        <Login />
      </div>
    );
  }
}

export default LoginScreen;
