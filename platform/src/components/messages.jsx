import React, { Component } from "react";
import Message from "./message";

class Messages extends Component {
  state = {};

  scrollToBottom = (id) => {
    try {
      const element = document.getElementById(id);
      element.scrollTop = element.scrollHeight;
    } catch (TypeError) {
      console.log("Its ok");
    }
  };

  render() {
    return (
      <div
        className="messages"
        id="messages"
        onLoad={this.scrollToBottom("messages")}
      >
        {this.props.messages.map((m) => {
          // TO BE CHANGED WHEN BACKEND DONE
          if (m.conversationID === this.props.cid)
            return <Message message={m} key={m.ID} user={this.props.user} />;
          return null;
        })}
      </div>
    );
  }
}

export default Messages;
