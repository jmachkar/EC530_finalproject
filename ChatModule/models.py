from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class MessageModel(db.Model):
    ID = db.Column(db.Integer,primary_key=True)
    senderID = db.Column(db.Integer, nullable=False)
    conversationID = db.Column(db.Integer,nullable=False)
    content = db.Column(db.String,nullable=False)
    timeStamp = db.Column(db.DateTime,nullable=False)
    def __init__(self, senderID:int, conversationID: int, content: str) -> None:
        self.senderID = senderID
        self.conversationID = conversationID
        self.content = content
        self.timeStamp = datetime.utcnow()
    
class UserModel(db.Model):
    ID = db.Column(db.Integer,primary_key=True)
    firstName = db.Column(db.String,nullable=False)
    lastName = db.Column(db.String,nullable=False)
    password = db.Column(db.String, nullable=False)
    def __init__(self, firstName: str, lastName: str, password: str) -> None:
        self.firstName = firstName
        self.lastName = lastName
        self.password = password

class ConversationModel(db.Model):
    ID = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Integer,nullable=True)
    def __init__(self, name: str = None):
        self.name = name

class ParticipantModel(db.Model):
    ID = db.Column(db.Integer,primary_key=True)
    userID = db.Column(db.Integer,nullable=False)
    conversationID = db.Column(db.Integer,nullable=False)
    joinedDateTime = db.Column(db.DateTime,nullable=False)
    leftDateTime = db.Column(db.DateTime,nullable=False)
    def __init__(self) -> None:                       
        self.joinedDateTime = datetime.utcnow()
        self.leftDateTime = None



    
