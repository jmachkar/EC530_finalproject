import React, { Component } from "react";

class Login extends Component {
  state = {};
  render() {
    return (
      <div className="login-box">
        <div>
          <label htmlFor="username" className="text-u">
            Username
          </label>
          <input type="text" name="username" placeholder="Username"></input>
        </div>
        <div>
          <label htmlFor="password">Password</label>
          <input type="password" name="password" placeholder="Password"></input>
        </div>
        <button
          type="submit"
          className="btn btn-secondary"
          onClick={console.log("Logged in")}
        >
          Login
        </button>
      </div>
    );
  }
}

export default Login;
