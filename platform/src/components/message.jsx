import React, { Component } from "react";

class Message extends Component {
  state = {
    message: this.props.message,
  };
  render() {
    return (
      <div
        className={
          this.state.message.username === this.props.user
            ? "message-content-sent"
            : "message-content-received"
        }
      >
        <div className="message-username">{this.state.message.username}</div>
        <div>{this.state.message.content}</div>
      </div>
    );
  }
}

export default Message;
