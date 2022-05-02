import React, { Component } from "react";

class ChatTag extends Component {
  state = {
    chat: { id: this.props.id, name: this.props.name },
    updated: false,
  };
  render() {
    return (
      <div
        className="chat-tag"
        onClick={() => this.props.onClick(this.state.chat)}
      >
        <p className="group-name-tag">{this.state.chat.name}</p>
      </div>
    );
  }
}

export default ChatTag;
