from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from matplotlib.style import use

db = SQLAlchemy()

class MessageModel(db.Model):
    ID = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String, nullable=False)
    conversationID = db.Column(db.Integer,nullable=False)
    content = db.Column(db.String,nullable=False)
    timeStamp = db.Column(db.DateTime,nullable=False)
    def __init__(self, username:str, conversationID: int, content: str) -> None:
        self.username = username
        self.conversationID = conversationID
        self.content = content
        self.timeStamp = datetime.utcnow()
    
class UserModel(db.Model):
    ID = db.Column(db.Integer,primary_key=True)
    firstName = db.Column(db.String,nullable=False)
    lastName = db.Column(db.String,nullable=False)
    username = db.Column(db.String,nullable=False)
    password = db.Column(db.String, nullable=False)
    role = db.Column(db.String, nullable=False)
    def __init__(self, firstName: str, lastName: str, username: str, password: str, role: str) -> None:
        self.firstName = firstName
        self.lastName = lastName
        self.username = username
        self.password = password
        self.role = role

class ConversationModel(db.Model):
    ID = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Integer,nullable=True)
    admin = db.Column(db.String,nullable=False)
    def __init__(self, admin: str, name: str = None):
        self.name = name
        self.admin = admin

class ParticipantModel(db.Model):
    ID = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String,nullable=False)
    conversationID = db.Column(db.Integer,nullable=False)
    joinedDateTime = db.Column(db.DateTime,nullable=False)
    leftDateTime = db.Column(db.DateTime,nullable=True)
    def __init__(self, username, conversationID) -> None: 
        self.username = username
        self.conversationID = conversationID                      
        self.joinedDateTime = datetime.utcnow()
        self.leftDateTime = None



    
