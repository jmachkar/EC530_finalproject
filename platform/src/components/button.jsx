import React, { Component } from "react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";

class SignInButton extends Component {
  state = {
    role: this.props.role,
    icon: this.props.icon,
  };
  render() {
    return (
      <div className="m-2">
        <FontAwesomeIcon icon={this.state.icon} />
        <button type="button" className="btn btn-primary btn-lg m-2">
          {this.state.role}
        </button>
      </div>
    );
  }
}

export default SignInButton;
