# EC530 Final Project

Team members:

- Jean Marc Achkar, jmachkar@bu.edu
- Daniel Cabrera, dcabrera@bu.edu
- John Mikulskis, jkulskis@bu.edu

## Project Overview

For our final project, we decided to make a web app for students and teachers to be able to chat with each other using a centralized system. Our web app supports private conversations in addition to group chats.

## Tech Specs

- Frontend:
  - Javascript
  - React
  - css
  - HTML
- APIs and servers:
  - Python
  - Flask
- Database:
  - SQLite

## TODO

### Frontend

- [x] Login screen with different roles
- [x] Chat screen with chats and messages
- [x] Add a new conversation
- [ ] Implement an admin screen to add users
- [ ] Implement a grades screen for students
- [ ] Implement a add new grade screen for teachers
- [ ] Tab bar navigation to redirect to grades dashboard

### Backend

- [x] Relational database models for messaging
  - [x] User model
  - [x] Message model
  - [x] Conversation model
  - [x] Participants model
- [x] Create POST and GET methods for each resource
- [x] Error checking
- [ ] Web sockets for notification system
- [ ] Relational database model for grade system
  - [ ] Grades model
  - [ ] Class model

## Run Locally

- Open two terminal sessions within the project directory.
- In terminal 1, run `cd ./ChatModule`
- Run `pip install -r requirements.txt`
- Run the API server `python chatServer.py`
- In terminal 2, run `cd ./platform`
- Run `npm install`
- Run the web hosting server `npm start` (this should open a web page on your browser with the url "http://localhost:3000")

## How to Use

The home page is where users can log in using their credentials. You must first select your role by clicking on the corresponding button.

<img src="./platform/src/images/homePage.png" alt="Home Screen" width=600/>

When you click on your desired role, a login form will pop up asking for your username and password. These fields are required in order to move to the next screen. Changing your role will dynamically update the form to show the selected role.

<img src="./platform/src/images/loginPage.png" alt="Login Screen" width=600/>

When you click on the login button, an API call will be made to authenticate the user and check if the user exists in the database and whether the password is correct or not.

If the user does not exist, or the password was incorrect, an alert will be displayed on the window.

<img src="./platform/src/images/wrongLogin.png" alt="Login error alert" width=600/>

If the user does exist, they will be redirected to the chat screen.

<img src="./platform/src/images/chatPage.png" alt="Initial chat screen" width=600/>

The chat app will load up all the chats this user is part of and display them on the side-bar to the left. A user can click on any of their chats to display the messages and send messages to that chat.

<img src="./platform/src/images/messagesPage.png" alt="Messages screen" width=600/>

The messages will be displayed in order of their sent time, and the username of the person who sent the message will show up above the message bubble.

The user can send messages either by clicking the enter key, or by clicking on the arrow button on the bottom right of the screen.

A new chat can be created by clicking on the plus button by "Chats" on the top left of the screen.
This will open a draggable form on the same window prompting the user for a group name and the username of the participants they would like to add to the chat seperated by white spaces.

<img src="./platform/src/images/addGroup.png" alt="Messages screen" width=600/>

Upon clicking on create, the new group will be added to the user's list of chats and all the participants will be added to the conversation provided their username exists on the database.

![image](https://user-images.githubusercontent.com/75552982/166407327-cde39f5a-3af6-44f2-a8a8-a84db857b23f.png)
https://www.youtube.com/watch?v=xL_tYrEcP9M
