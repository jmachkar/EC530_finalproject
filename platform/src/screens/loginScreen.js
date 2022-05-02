import React, { Component } from "react";
import {
  faSchool,
  faGraduationCap,
  faDesktop,
} from "@fortawesome/free-solid-svg-icons";

import "../components/login.css";
import Buttons from "../components/buttons";
import Login from "../components/loginBox";
import { LoginUser, callLogin } from "../backend/loginRequest";

class LoginScreen extends Component {
  state = {
    curr: { username: "", password: "", role: "" },
    v: "login-box-hidden",
    roles: [
      { key: "Student", icon: faSchool },
      { key: "Teacher", icon: faGraduationCap },
      { key: "Admin", icon: faDesktop },
    ],
    currRole: "",
  };

  showLogin = (role) => {
    const v = "login-box-visible";
    const currRole = role;
    const curr = {
      username: this.state.curr.username,
      password: this.state.curr.password,
      role: role,
    };
    this.setState({ v, currRole, curr });
    console.log(this.state.v);
    console.log(this.state.curr);
  };

  closeLogin = () => {
    const v = "login-box-hidden";
    this.setState({ v });
    console.log(this.state.v);
  };

  handleLogin = () => {
    let result = LoginUser(this.state.curr);
    // console.log(this.state.curr.username);
    // console.log(this.state.curr.password);
    // console.log(result);
  };

  handleUserChange = (user) => {
    const curr = {
      username: user,
      password: this.state.curr.password,
      role: this.state.currRole,
    };
    this.setState({ curr });
  };

  handlePasswordChange = (password) => {
    const curr = {
      username: this.state.curr.username,
      password: password,
      role: this.state.currRole,
    };
    this.setState({ curr });
  };

  render() {
    return (
      <div className="main-login">
        <h1>Welcome to the platform!</h1>
        <h2>Please chosose your role</h2>
        <Buttons onClick={this.showLogin} roles={this.state.roles} />
        <Login
          visibility={this.state.v}
          role={this.state.currRole}
          close={this.closeLogin}
          userChange={this.handleUserChange}
          passwordChange={this.handlePasswordChange}
          login={this.handleLogin}
        />
      </div>
    );
  }
}

export default LoginScreen;
