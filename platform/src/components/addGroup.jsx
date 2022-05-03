import React, { Component } from "react";
import Draggable from "react-draggable";

class AddGroupForm extends Component {
  state = {
    name: "",
    participants: [],
  };

  updateGroup = (name) => {
    this.setState({ name });
  };

  updateParticipants = (e) => {
    const participants = e.target.value.split(" ");
    this.setState({ participants });
  };

  render() {
    return (
      <Draggable>
        <div id="grp-form" className={this.props.v}>
          <div className="form">
            <div className="input-grp-name">
              <label>Group Name: </label>
              <input
                type="text"
                onChange={(e) => this.updateGroup(e.target.value)}
              ></input>
            </div>
            <div className="input-grp-name">
              <label> Participant usernames: </label>
              <textarea
                className="input-grp-name-text"
                type="text"
                placeholder="Seperate with spaces"
                onChange={(e) => this.updateParticipants(e)}
              ></textarea>
            </div>

            <button
              onClick={() => {
                this.props.onCreate(this.state.name, this.state.participants);
                this.setState({ v: "form-hidden" });
              }}
            >
              Create
            </button>
          </div>
        </div>
      </Draggable>
    );
  }
}

export default AddGroupForm;
