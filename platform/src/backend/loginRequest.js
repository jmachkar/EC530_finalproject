import React from "react";

const BASE = "http://127.0.0.1:5000";

// Do get requests here
export async function LoginUser(curr) {
  // let response = await fetch(
  //   BASE + "/users/" + curr.username + "/" + curr.password
  // );
  // let result = response.json;
  // console.log(result);
  // return result;
  fetch(BASE + "/users/" + curr.username + "/" + curr.password).then(
    (response) => {
      if (response.status !== 200) {
        alert("Wrong username or password");
      } else {
        var pw = [];
        for (let index = 0; index < curr.password.length; index++) {
          const code = curr.password.charCodeAt(index);
          pw.push(code);
        }
        window.location.assign(
          `http://localhost:3000/chat/${curr.role}/${curr.username}/${pw.join(
            "-"
          )}`
        );
      }
    }
  );
}

export function getConvos(username, password) {
  fetch(BASE + "/conversations/" + username + "/" + password)
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
    });
}
