import React, { Component } from "react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";

class SignInButton extends Component {
  state = {
    role: this.props.role,
    icon: this.props.icon,
  };

  render() {
    return (
      <div className="button-box">
        <FontAwesomeIcon icon={this.state.icon} />
        <button
          type="button"
          className="btn btn-primary btn-lg m-2"
          onClick={() => this.props.onClick(this.state.role)}
        >
          {this.state.role}
        </button>
      </div>
    );
  }
}

export default SignInButton;
