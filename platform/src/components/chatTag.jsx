import React, { Component } from "react";

class ChatTag extends Component {
  state = {
    chat: { id: this.props.id, name: this.props.name },
    updated: false,
  };
  render() {
    return (
      <div>
        <p onClick={() => this.props.onClick(this.state.chat)}>
          {this.state.chat.name}
        </p>
      </div>
    );
  }
}

export default ChatTag;
