import React, { Component } from "react";
import ChatTag from "./chatTag";
import { faCirclePlus } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import AddGroupForm from "./addGroup";

class ChatTags extends Component {
  state = {
    v: "form-hidden",
  };

  showForm = () => {
    if (this.state.v === "form-hidden") {
      this.setState({ v: "form-visible" });
    } else {
      this.setState({ v: "form-hidden" });
    }
  };

  render() {
    return (
      <div className="side-bar">
        <AddGroupForm v={this.state.v} onCreate={this.props.addGroup} />
        <div className="chats-header-box">
          <b className="chats-header">Chats</b>
          <button className="add-grp" onClick={() => this.showForm()}>
            <FontAwesomeIcon icon={faCirclePlus} />
          </button>
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
