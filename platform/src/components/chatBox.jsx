import React, { Component } from "react";
import Messages from "./messages";
import { faArrowRight } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";

class ChatBox extends Component {
  state = {
    key: -1,
    message: "",
  };

  handleOnChange = (message) => {
    this.setState({ key: this.props.messages.length, message });
  };

  handleClear = () => {
    console.log(this.props.messages);
    this.setState({ key: -1, message: "" });
  };

  onEnterPress = (e) => {
    if (e.keyCode === 13 && e.shiftKey === false) {
      e.preventDefault();
      this.props.send({
        key: this.props.messages.length,
        message: e.target.value,
        cid: this.props.curr.id,
        sent: true,
      });
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
          <Messages messages={this.props.messages} cid={this.props.curr.id} />
          <div className="input-box">
            <textarea
              className="input"
              value={this.state.message}
              required
              onChange={(e) => this.handleOnChange(e.target.value)}
              onKeyDown={(e) => this.onEnterPress(e)}
            />
            <div
              className="send-button"
              onClick={() => {
                this.props.send(
                  Object.assign(this.state, {
                    cid: this.props.curr.id,
                    sent: true,
                  })
                );
                this.handleClear();
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
