import React, { Component } from "react";

class Message extends Component {
  state = {
    message: this.props.message,
  };
  render() {
    return (
      // <div
      //   className={
      //     this.state.message.sent ? "message-sent" : "message-received"
      //   }
      // >
      <div
        className={
          this.state.message.sent
            ? "message-content-sent"
            : "message-content-received"
        }
      >
        {this.state.message.message}
      </div>
      /* </div> */
    );
  }
}

export default Message;
