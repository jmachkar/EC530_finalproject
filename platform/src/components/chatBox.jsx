import React, { Component } from "react";
import Messages from "./messages";
import { faArrowRight } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";

class ChatBox extends Component {
  state = {
    cid: this.props.curr.id,
    content: "",
  };

  handleOnChange = (content) => {
    this.setState({ content });
  };

  handleClear = () => {
    console.log(this.props.messages);
    this.setState({ content: "" });
  };

  onEnterPress = (e) => {
    if (e.keyCode === 13 && e.shiftKey === false) {
      e.preventDefault();
      this.props.send(this.state.content);
      this.handleClear();
    }
  };

  // Fetch messages with id and setstate
  render() {
    return (
      <div className="chat-box">
        <div className="chat-name-box">
          <b className="chat-name">{this.props.curr.name}</b>
        </div>
        <div className="message-type-box">
          <Messages
            messages={this.props.messages}
            cid={this.props.curr.id}
            user={this.props.user}
          />
          <div className="input-box">
            <textarea
              className="input"
              value={this.state.content}
              required
              onChange={(e) => this.handleOnChange(e.target.value)}
              onKeyDown={(e) => this.onEnterPress(e)}
            />
            <div
              className="send-button"
              onClick={() => {
                this.props.send(this.state.content);
                this.handleClear();
                console.log("this happened");
              }}
            >
              <FontAwesomeIcon className="send-icon" icon={faArrowRight} />
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default ChatBox;
