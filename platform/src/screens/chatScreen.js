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
      { key: 0, message: "hello", cid: 0 },
      { key: 1, message: "hi", cid: 0 },
      { key: 2, message: "yooooooo", cid: 0 },
      { key: 3, message: "eyooo", cid: 1 },
      { key: 4, message: "fdjfhs", cid: 1 },
      { key: 5, message: "yo", cid: 2 },
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

  render() {
    return (
      <div>
        <h1>Chats</h1>
        <ChatTags chats={this.state.chats} onClick={this.handleOnClick} />
        <ChatBox curr={this.state.curr} messages={this.state.messages} />
      </div>
    );
  }
}

export default ChatScreen;
