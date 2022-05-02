import React, { Component } from "react";
import Message from "./message";

class Messages extends Component {
  state = {};
  render() {
    return (
      <div className="messages">
        {this.props.messages.map((m) => {
          // TO BE CHANGED WHEN BACKEND DONE
          if (m.cid === this.props.cid)
            return <Message message={m} key={m.key} />;
          return null;
        })}
      </div>
    );
  }
}

export default Messages;
