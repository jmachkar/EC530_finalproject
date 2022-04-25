import React, { Component } from "react";
import "../components/login.css";
import Buttons from "../components/buttons";
import Login from "../components/loginBox";
import Title from "../components/Title";

class LoginScreen extends Component {
  state = {};
  render() {
    return (
      <div className="body">
        <div className="header">
          <Title />
        </div>
        <div className="main">
          <div className="loginBox">
            <Buttons />
            <Login />
          </div>
        </div>
      </div>
    );
  }
}

export default LoginScreen;
