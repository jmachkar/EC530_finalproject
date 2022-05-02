import React, { Component } from "react";

class Login extends Component {
  state = {};
  render() {
    return (
      <div className={this.props.visibility} id="loginBox">
        <div className="close" onClick={this.props.close}>
          x
        </div>
        <h1>{this.props.role}</h1>
        <div className="input-container">
          <label htmlFor="username" className="text-u">
            Username
          </label>
          <input
            type="text"
            name="username"
            placeholder="Username"
            onChange={(e) => this.props.userChange(e.target.value)}
          ></input>
        </div>
        <div className="input-container">
          <label htmlFor="password">Password</label>
          <input
            type="password"
            name="password"
            placeholder="Password"
            onChange={(e) => this.props.passwordChange(e.target.value)}
          ></input>
        </div>
        <button
          type="submit"
          className="submit"
          onClick={
            () => this.props.login() /* call get request function here */
          }
        >
          Login
        </button>
      </div>
    );
  }
}

export default Login;
