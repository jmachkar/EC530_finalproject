import React, { Component } from "react";
import Messages from "./messages";

class ChatBox extends Component {
  state = {};

  // Fetch messages with id and setstate
  render() {
    return (
      <div>
        <div>
          <b>{this.props.curr.name}</b>
        </div>
        <div>
          <Messages messages={this.props.messages} cid={this.props.curr.id} />
        </div>
      </div>
    );
  }
}

export default ChatBox;
