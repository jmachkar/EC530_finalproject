import React, { Component } from "react";
import "../components/login.css";
import Buttons from "../components/buttons";
import Login from "../components/loginBox";
import {
  faSchool,
  faGraduationCap,
  faDesktop,
} from "@fortawesome/free-solid-svg-icons";

class LoginScreen extends Component {
  state = {
    v: "login-box-hidden",
    roles: [
      { key: "Student", icon: faSchool },
      { key: "Teacher", icon: faGraduationCap },
      { key: "Admin", icon: faDesktop },
    ],
    curr: "",
  };

  showLogin = (role) => {
    let v = "login-box-visible";
    let newState = {
      v: v,
      roles: [
        { key: "Student", icon: faSchool },
        { key: "Teacher", icon: faGraduationCap },
        { key: "Admin", icon: faDesktop },
      ],
      curr: role,
    };
    this.setState(newState);
    console.log(this.state.v);
  };

  render() {
    return (
      <div className="main">
        <h1>Welcome to the platform!</h1>
        <h2>Please chosose your role</h2>
        <Buttons onClick={this.showLogin} roles={this.state.roles} />
        <Login visibility={this.state.v} role={this.state.curr} />
      </div>
    );
  }
}

export default LoginScreen;
