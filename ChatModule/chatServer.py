from flask import Flask, abort
from flask_cors import CORS
from flask_restx import Api, Resource, reqparse, fields
from models import db, MessageModel, ConversationModel, ParticipantModel, UserModel
from datetime import datetime

app = Flask(__name__)
CORS(app)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chatDatabase.db'
db.init_app(app)
with app.app_context():
    db.create_all()

msgFields = api.model(
    'Message', 
    {
        'ID': fields.Integer,
        'username': fields.String,
        'conversationID': fields.Integer,
        'content': fields.String,
        'timeStamp': fields.DateTime
    }
)

postMsgArgs = reqparse.RequestParser(bundle_errors=True)
postMsgArgs.add_argument('username',type=str, required=True)
postMsgArgs.add_argument('password',type=str,required=True)
postMsgArgs.add_argument('conversationID',type=int,required=True)
postMsgArgs.add_argument('content',type=str,required=True)

getMsgArgs = reqparse.RequestParser(bundle_errors=True)
getMsgArgs.add_argument('username',type=str, required=True)
getMsgArgs.add_argument('password',type=str, required=True)
getMsgArgs.add_argument('conversationID',type=int, required=True)
getMsgArgs.add_argument('content',type=str,required=False)

class MsgResource(Resource):
    @api.marshal_with(msgFields,code=201)
    def post(self):
        args = postMsgArgs.parse_args()
        conversation = ConversationModel.query.get(args['conversationID'])
        if conversation is None:
            abort(409, 'conversation does not exist')
        user = UserModel.query.filter(UserModel.username == args['username']).first()
        if user is None:
            abort(401)
        if user.password != args['password']:
            abort(401)
        msg = MessageModel(
            username = args['username'],
            conversationID = args['conversationID'],
            content = args['content']
        )
        db.session.add(msg)
        db.session.flush()
        db.session.commit()
        return msg
    @api.marshal_with(msgFields, code=200)
    def get(self):
        args = getMsgArgs.parse_args()
        user = UserModel.query.filter(UserModel.username == args['username']).first()
        if user is None:
            abort(401)
        if user.password != args['password']:
            abort(401)
        participants = ParticipantModel.query.filter(ParticipantModel.conversationID == args['conversationID'])
        participant = participants.filter(ParticipantModel.username == args['username']).first()
        if participant is None:
            abort(403)
        msgsQuery = MessageModel.query.filter(MessageModel.conversationID == args['conversationID'])
        msgsQuery = msgsQuery.filter(MessageModel.timeStamp >= participant.joinedDateTime)
        if args['content'] is not None:
            search = "%{}%".format(args['content'])
            msgsQuery = msgsQuery.filter(MessageModel.content.like(search))
        return msgsQuery.all()

convFields = api.model(
    'Conversation', 
    {
        'ID': fields.Integer,
        'name': fields.String
    }
)
postConvArgs = reqparse.RequestParser(bundle_errors=True)
postConvArgs.add_argument('name',type=str, required=False)
postConvArgs.add_argument('username',type=str, required=True)
postConvArgs.add_argument('password',type=str, required=True)

getConvArgs = reqparse.RequestParser(bundle_errors=True)
getConvArgs.add_argument('username',type=str, required=True)
getConvArgs.add_argument('password',type=str, required=True)
class ConversationResource(Resource):
    @api.marshal_with(convFields,code=201)
    def post(self):
        args = postConvArgs.parse_args()
        user = UserModel.query.filter(UserModel.username == args['username']).first()
        if user is None:
            abort(401)
        if user.password != args['password']:
            abort(401)
        conversation = ConversationModel(
            name = args['name'],
            admin = args['username']
        )
        db.session.add(conversation)
        db.session.flush()
        db.session.commit()
        participant = ParticipantModel(
            username = args['username'],
            conversationID = conversation.ID
        )
        db.session.add(participant)
        db.session.flush()
        db.session.commit()
        return conversation
    @api.marshal_with(convFields,code=200)
    def get(self, username, password):
        # args = getConvArgs.parse_args()
        # user = UserModel.query.filter(UserModel.username == args['username']).first()
        user = UserModel.query.filter(UserModel.username == username).first()

        if user is None:
            abort(401)
        # if user.password != args['password']:
        #     abort(401)
        if user.password != password:
            abort(401)
        # memberships = ParticipantModel.query.filter(ParticipantModel.username == args['username']).all()
        memberships = ParticipantModel.query.filter(ParticipantModel.username == username).all()
        conversations = []
        for membership in memberships:
            conversations.append(ConversationModel.query.get(membership.conversationID))
        return conversations

participantFields = api.model(
    'Participant', 
    {
        'username': fields.String,
        'conversationID': fields.String,
        'joinedDateTime': fields.DateTime,
        'leftDateTime': fields.DateTime
    }
)
postParticipantArgs = reqparse.RequestParser(bundle_errors=True)
postParticipantArgs.add_argument('conversationID',type=int, required=True)
postParticipantArgs.add_argument('admin', type=str, required=True)
postParticipantArgs.add_argument('password', type=str, required=True)
postParticipantArgs.add_argument('participant', type=str, required=True)

getParticipantArgs = reqparse.RequestParser(bundle_errors=True)
getParticipantArgs.add_argument('username',type=str, required=False)
getParticipantArgs.add_argument('conversationID',type=int, required=False)
getParticipantArgs.add_argument('joinedDateTime',type=datetime, required=False)
class ParticipantResource(Resource):
    @api.marshal_with(participantFields, code=201)
    def post(self):
        args = postParticipantArgs.parse_args()
        conversation = ConversationModel.query.get(args['conversationID'])
        if conversation is None:
            abort(409, 'conversation does not exist')
        if conversation.admin != args['admin']:
            abort(401)
        admin = UserModel.query.filter(UserModel.username == conversation.admin).first()
        if admin.password != args['password']:
            abort(401)
        participants = ParticipantModel.query.filter(ParticipantModel.conversationID == args['conversationID'])
        participant = participants.filter(ParticipantModel.username == args['participant']).first()
        if participant is None:
            print('None')
        else:
            print('not None')
        if participant is not None:
            abort(409, 'participant already added')
        participant = ParticipantModel(
            username = args['participant'],
            conversationID = args['conversationID']
        )
        db.session.add(participant)
        db.session.flush()
        db.session.commit()
        return participant
    @api.marshal_with(participantFields, code=200)
    def get():
        args = getParticipantArgs.parse_args()
        participantsQuery = ParticipantModel.query.filter(ParticipantModel.userID != None)
        if args['userID'] is not None:
            participantsQuery = participantsQuery.filter(ParticipantModel.userID == args['userID'])
        if args['conversationID'] is not None:
            participantsQuery = participantsQuery.filter(ParticipantModel.conversationID == args['conversationID'])
        return participantsQuery.all()

userFields = api.model(
    'User', 
    {
        'username': fields.String,
        'firstName': fields.String,
        'lastName': fields.String,
        'role': fields.String
    }
)
postUserArgs = reqparse.RequestParser(bundle_errors=True)
postUserArgs.add_argument('firstName',type=str,required=True)
postUserArgs.add_argument('lastName',type=str,required=True)
postUserArgs.add_argument('username',type=str,required=True)
postUserArgs.add_argument('password',type=str,required=True)
postUserArgs.add_argument('role',type=str,required=True)

# getUserArgs = reqparse.RequestParser(bundle_errors=True)
# getUserArgs.add_argument('username',type=str,required=True)
class UserResource(Resource):
    @api.marshal_with(userFields, code=201)
    def post(self):
        args = postUserArgs.parse_args()
        user = UserModel.query.filter(UserModel.username == args['username']).first()
        if user is not None:
            abort(409, 'username already exists')
        user = UserModel(
            firstName = args['firstName'],
            lastName = args['lastName'],
            username = args['username'],
            password = args['password'],
            role = args['role']
        )
        db.session.add(user)
        db.session.flush()
        db.session.commit()
        return user
    @api.marshal_with(userFields,code=200)
    def get(self,username,password):
        # args = getUserArgs.parse_args()
        # user = UserModel.query.filter(UserModel.username == args['username']).first()
        user = UserModel.query.filter(UserModel.username == username).first()
        if user is None:
            print("Here")
            abort(401)
        if user.password != password:
            abort(401)
        return user

api.add_resource(MsgResource,'/messages/')
api.add_resource(ConversationResource,'/conversations/')
api.add_resource(ConversationResource,'/conversations/<string:username>/<string:password>')
api.add_resource(ParticipantResource,'/participants/')
api.add_resource(UserResource,'/users/')
api.add_resource(UserResource,'/users/<string:username>/<string:password>')

if __name__ == '__main__':
    app.run(debug=True)