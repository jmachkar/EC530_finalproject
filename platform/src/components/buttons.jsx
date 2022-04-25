import React, { Component } from "react";
import SignInButton from "./button";

class Buttons extends Component {
  state = {};
  render() {
    return (
      <div className="btn-group" role="group" aria-label="Basic example">
        {this.props.roles.map((role) => (
          <SignInButton
            key={role.key}
            role={role.key}
            icon={role.icon}
            onClick={this.props.onClick}
          />
        ))}
      </div>
    );
  }
}

export default Buttons;
