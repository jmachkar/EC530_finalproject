import React, { Component } from "react";
import ChatTag from "./chatTag";

class ChatTags extends Component {
  state = {};
  render() {
    return (
      <div className="chat-tags">
        <div className="chats-header-box">
          <b className="chats-header">Chats</b>
        </div>
        {this.props.chats.map((chat) => (
          <ChatTag
            key={chat.id}
            name={chat.name}
            id={chat.id}
            onClick={this.props.onClick}
          />
        ))}
      </div>
    );
  }
}

export default ChatTags;
