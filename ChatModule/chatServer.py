from flask import Flask, abort
from flask_restx import Api, Resource, reqparse, fields
from models import db, MessageModel, ConversationModel, ParticipantModel, UserModel
from datetime import datetime

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chatDatabase.db'


msgFields = api.model(
    'Message', 
    {
        'ID': fields.Integer,
        'senderID': fields.Integer,
        'conversationID': fields.Integer,
        'content': fields.String,
        'timeStamp': fields.DateTime
    }
)

postMsgArgs = reqparse.RequestParser(bundle_errors=True)
postMsgArgs.add_argument('senderID',type=int, required=True)
postMsgArgs.add_argument('conversationID',type=int,required=True)
postMsgArgs.add_argument('content',type=str,required=True)

getMsgArgs = reqparse.RequestParser(bundle_errors=True)
getMsgArgs.add_argument('senderID',type=int, required=False)
getMsgArgs.add_argument('conversationID',type=int,required=False)
getMsgArgs.add_argument('content',type=str,required=False)
getMsgArgs.add_argument('timeStamp',type=datetime,required=False)

class MsgResource(Resource):
    @api.marshal_with(code=201)
    def post(self):
        args = postMsgArgs.parse_args()
        msg = MessageModel(
            senderID = args['senderID'],
            conversationID = args['conversationID'],
            content = args['content']
        )
        db.session.add(msg)
        db.session.flush()
        db.session.commit()
        return
    @api.marshal_with(msgFields, code=200)
    def get(self):
        args = getMsgArgs.parse_args()
        msgsQuery = MessageModel.query.filter_by(MessageModel.senderID != None)
        if args['senderID'] is not None:
            msgsQuery = msgsQuery.filter_by(MessageModel.senderID == args['senderID'])
        if args['conversationID'] is not None:
            msgsQuery = msgsQuery.filter_by(MessageModel.conversationID == args['conversationID'])
        if args['timeStamp'] is not None:
            msgsQuery = msgsQuery.filter_by(MessageModel.timeStamp >= args['timeStamp'])
        if args['content'] is not None:
            search = "%{}%".format(args['content'])
            msgsQuery = msgsQuery.filter_by(MessageModel.content.like(search))
        return msgsQuery.all()

convFields = api.model(
    'Conversation', 
    {
        'ID': fields.Integer,
        'name': fields.String
    }
)
class ConversationResource(Resource):
    @api.marshal_with(convFields,code=201)
    def post(name):
        conversation = ConversationModel(
            name = name
        )
        db.session.add(conversation)
        db.session.flush()
        db.session.commit()
        return conversation
    @api.marshal_width(convFields,code=200)
    def get(ID):
        conversation = ConversationModel.query.get(ID)
        return conversation

participantFields = api.model(
    'Participant', 
    {
        'userID': fields.Integer,
        'conversationID': fields.String,
        'joinedDateTime': fields.DateTime,
        'leftDateTime': fields.DateTime
    }
)
postParticipantArgs = reqparse.RequestParser(bundle_errors=True)
postParticipantArgs.add_argument('userID',type=int, required=True)
postParticipantArgs.add_argument('conversationID',type=int, required=True)

getParticipantArgs = reqparse.RequestParser(bundle_errors=True)
getParticipantArgs.add_argument('userID',type=int, required=False)
getParticipantArgs.add_argument('conversationID',type=int, required=False)
getParticipantArgs.add_argument('joinedDateTime',type=datetime, required=False)
class ParticipantResource(Resource):
    @api.marshal_with(code=201)
    def post():
        args = postParticipantArgs.parse_args()
        participant = ParticipantModel(
            userID = args['userID'],
            conversationID = args['conversationID']
        )
        db.session.add(participant)
        db.session.commit()
        return
    @api.marshal_with(participantFields, code=200)
    def get():
        args = getParticipantArgs.parse_args()
        participantsQuery = ParticipantModel.query.filter_by(ParticipantModel.userID != None)
        if args['userID'] is not None:
            participantsQuery = participantsQuery.filter_by(ParticipantModel.userID == args['userID'])
        if args['conversationID'] is not None:
            participantsQuery = participantsQuery.filter_by(ParticipantModel.conversationID == args['conversationID'])
        return participantsQuery.all()

userFields = api.model(
    'User', 
    {
        'ID': fields.Integer,
        'firstName': fields.String,
        'lastName': fields.String
    }
)
postUserArgs = reqparse.RequestParser(bundle_errors=True)
postUserArgs.add_argument('firstName',type=str,required=True)
postUserArgs.add_argument('lastName',type=str,required=True)
class UserResource(Resource):
    @api.marshal_width(code=201)
    def post(ID):
        args = postUserArgs.parse_args()
        user = UserModel(
            ID = ID,
            firstName = args['firstName'],
            lastName = args['lastName']
        )
        try:
            db.session.add(user)
            db.session.commit()
        except:
            abort(400,description="ID likely already exists")
        return 
    @api.marshal_with(userFields,code=200)
    def get(ID):
        user = UserModel.query.get(ID)
        return user

api.add_resource(MsgResource,'/messages/')
api.add_resource(ConversationResource,'/conversations/')
api.add_resource(ParticipantResource,'/participants/')
api.add_resource(UserResource,'/users/')

if __name__ == '__main__':
    app.run(debug=True)