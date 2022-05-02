import React, { Component } from "react";
import ChatBox from "../components/chatBox";
import ChatTags from "../components/chatTags";

class ChatScreen extends Component {
  state = {
    chats: [
      { id: 0, name: "Group 1" },
      { id: 1, name: "Group 2" },
      { id: 2, name: "Group 3" },
    ],
    curr: { id: -1, name: "" },
    messages: [
      { key: 0, message: "hello", cid: 0, sent: true },
      { key: 1, message: "hi", cid: 0, sent: false },
      {
        key: 2,
        message: "yoooooooooooooooooooooooooooooooooooooooooooooooooo",
        cid: 0,
        sent: false,
      },
      { key: 3, message: "eyooo", cid: 1, sent: false },
      { key: 4, message: "fdjfhs", cid: 1, sent: true },
      { key: 5, message: "yo", cid: 2, sent: false },
    ],
  };

  handleOnClick = (group) => {
    const curr = group;
    //GET MESSAGES
    // const messages = newchats
    this.setState({ curr }); // setstate messages
    console.log("Clicked on " + group.name);
    console.log(this.state.curr);
  };

  handleOnSend = (message) => {
    if (message.message.length > 0 && message.cid > 0) {
      let messages = this.state.messages;
      messages.push(message);
      this.setState({ messages });
      console.log(message.message);
      console.log(message.sent);
    }
  };

  render() {
    return (
      <div className="main-chat">
        <div className="sub-main-chat">
          <ChatTags chats={this.state.chats} onClick={this.handleOnClick} />
          <ChatBox
            curr={this.state.curr}
            messages={this.state.messages}
            send={this.handleOnSend}
          />
        </div>
      </div>
    );
  }
}

export default ChatScreen;
