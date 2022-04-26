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
    const v = "login-box-visible";
    const curr = role;
    this.setState({ v, curr });
    console.log(this.state.v);
    console.log(this.state.curr);
  };

  closeLogin = () => {
    const v = "login-box-hidden";
    this.setState({ v });
    console.log(this.state.v);
  };

  render() {
    return (
      <div className="main">
        <h1>Welcome to the platform!</h1>
        <h2>Please chosose your role</h2>
        <Buttons onClick={this.showLogin} roles={this.state.roles} />
        <Login
          visibility={this.state.v}
          role={this.state.curr}
          close={this.closeLogin}
        />
      </div>
    );
  }
}

export default LoginScreen;
