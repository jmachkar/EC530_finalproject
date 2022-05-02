import React, { Component } from "react";
import ChatTag from "./chatTag";

class ChatTags extends Component {
  state = {};
  render() {
    return (
      <div className="side-bar">
        <div className="chats-header-box">
          <b className="chats-header">Chats</b>
        </div>
        <div className="chat-tags">
          {this.props.chats.map((chat) => (
            <ChatTag
              key={chat.ID}
              name={chat.name}
              id={chat.ID}
              onClick={this.props.onClick}
            />
          ))}
        </div>
      </div>
    );
  }
}

export default ChatTags;
