import React, { Component } from "react";
import ChatBox from "../components/chatBox";
import ChatTags from "../components/chatTags";

const BASE = "http://127.0.0.1:5000";

class ChatScreen extends Component {
  constructor() {
    super();
    this.state = {
      user: "",
      password: "",
      chats: [],
      curr: { id: -1, name: "" },
      messages: [],
    };
  }

  componentDidMount() {
    const out = this.getUserPassword();
    console.log("Ths is running again");
    fetch(BASE + "/conversations/" + out[0] + "/" + out[1])
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
          this.setState({ chats, user: out[0], password: out[1] });
          console.log(this.state.chats);
        }
        console.log("done get convos");
      });
  }

  state = {
    user: "",
    password: "",
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

  addGroup = (name, participants) => {
    // post group in convo table
    // post participants in prtc table
    fetch(
      BASE + "/conversations/" + this.state.user + "/" + this.state.password,
      {
        method: "POST",
        headers: {
          "Content-type": "application/json",
        },
        body: JSON.stringify({ name: name }),
      }
    )
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
      .then((conversation) => {
        if (conversation === undefined) {
          console.log("Something failed, conversation response is undefined");
        } else {
          let chats = this.state.chats;
          chats.push(conversation);
          this.setState({ chats });
          console.log("Posted new conversation");
          console.log({ chats });
          for (let index = 0; index < participants.length; index++) {
            const element = participants[index];
            fetch(
              BASE +
                "/participants/" +
                this.state.user +
                "/" +
                this.state.password +
                "/" +
                conversation.ID.toString(),
              {
                method: "POST",
                headers: {
                  "Content-type": "application/json",
                },
                body: JSON.stringify({ participant: element }),
              }
            )
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
              .then((participant) => {
                if (participant === undefined) {
                  console.log(
                    "Something failed, participant response is undefined"
                  );
                } else {
                  console.log(
                    "New participant " +
                      participant.username +
                      " added to convo " +
                      conversation.name
                  );
                }
              });
          }
        }
      });
  };

  getUserPassword = () => {
    const url = window.location.href;
    // console.log(url);
    const a = url.split("/");
    const user = a[5];
    // console.log(user);
    const pw = a[6];
    var pwList = pw.split("-");
    // console.log(pw);

    var password = "";
    for (let index = 0; index < pwList.length; index++) {
      const char = String.fromCharCode(pwList[index]);
      password += char;
    }
    // console.log(password);

    const out = [user, password];
    return out;
  };

  handleOnClick = (group) => {
    const curr = group;
    console.log(group);

    fetch(
      BASE +
        "/messages/" +
        this.state.user +
        "/" +
        this.state.password +
        "/" +
        group.id.toString()
    )
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
      .then((messages) => {
        if (messages === undefined) {
          this.setState({});
          console.log("empty");
        } else {
          this.setState({ curr, messages });
          // console.log(this.state.chats);
        }
        console.log("done get messages");
      });

    // this.setState({ curr }); // setstate messages
    console.log("Clicked on " + group.name);
    console.log(this.state.curr);
  };

  handleOnSend = (message) => {
    console.log(message + " " + this.state.curr.id);
    if (message.length > 0 && this.state.curr.id > 0) {
      fetch(
        BASE +
          "/messages/" +
          this.state.user +
          "/" +
          this.state.password +
          "/" +
          this.state.curr.id.toString(),
        {
          method: "POST",
          headers: {
            "Content-type": "application/json",
          },
          body: JSON.stringify({ content: message }),
        }
      )
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
        .then((newMessage) => {
          if (newMessage === undefined) {
            console.log("Something failed, newMessage response is undefined");
          } else {
            let messages = this.state.messages;
            messages.push(newMessage);
            this.setState({ messages });
            console.log("Here");
            console.log({ messages });
          }
        });
    }
    console.log("Done posting message");
  };

  render() {
    return (
      <div className="main-chat">
        <div className="sub-main-chat">
          <ChatTags
            chats={this.state.chats}
            onClick={this.handleOnClick}
            addGroup={this.addGroup}
          />
          <ChatBox
            curr={this.state.curr}
            messages={this.state.messages}
            send={this.handleOnSend}
            user={this.state.user}
            pw={this.state.password}
          />
        </div>
      </div>
    );
  }
}

export default ChatScreen;
