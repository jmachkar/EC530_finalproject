import React, { Component } from "react";
import SignInButton from "./button";
import {
  faSchool,
  faGraduationCap,
  faDesktop,
} from "@fortawesome/free-solid-svg-icons";

class Buttons extends Component {
  state = {
    roles: [
      { key: "Student", icon: faSchool },
      { key: "Teacher", icon: faGraduationCap },
      { key: "Admin", icon: faDesktop },
    ],
  };
  render() {
    return (
      <div class="btn-group" role="group" aria-label="Basic example">
        {this.state.roles.map((role) => (
          <SignInButton key={role.key} role={role.key} icon={role.icon} />
        ))}
      </div>
    );
  }
}

export default Buttons;
