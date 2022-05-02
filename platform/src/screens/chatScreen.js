import React, { Component } from "react";
import { getConvos } from "../backend/loginRequest";
import ChatBox from "../components/chatBox";
import ChatTags from "../components/chatTags";

class ChatScreen extends Component {
  constructor() {
    super();
    this.state = {
      chats: [],
      curr: { id: -1, name: "" },
      messages: [],
    };
  }

  componentDidMount() {
    const BASE = "http://127.0.0.1:5000";
    const url = window.location.href;
    console.log(url);
    const a = url.split("/");
    const user = a[5];
    console.log(user);
    const pw = a[6];
    var pwList = pw.split("-");
    console.log(pw);

    var password = "";
    for (let index = 0; index < pwList.length; index++) {
      const char = String.fromCharCode(pwList[index]);
      password += char;
    }
    console.log(password);
    // var chats = getConvos(user, password);

    fetch(BASE + "/conversations/" + user + "/" + password)
      .then((response) => {
        if (response.status !== 200) {
          alert("Something went wrong");
          console.log(response.statusText);
        } else {
          return response.json();
        }
      })
      .then((data) => {
        console.log(data);
        return data;
      })
      .then((chats) => {
        if (chats === undefined) {
          this.setState({});
          console.log("empty");
        } else {
          this.setState({ chats });
          console.log(this.state.chats);
        }
        console.log("done get convos");
      });
  }

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
      { key: 2, message: "yooooooo", cid: 0, sent: false },
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
