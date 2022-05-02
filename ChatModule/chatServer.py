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
        'username': fields.String,
        'conversationID': fields.Integer,
        'content': fields.String,
        'timeStamp': fields.DateTime
    }
)

postMsgArgs = reqparse.RequestParser(bundle_errors=True)
postMsgArgs.add_argument('content',type=str,required=True)
class MsgResource(Resource):
    @api.marshal_with(msgFields,code=201)
    def post(self,username,password,conversationID):
        args = postMsgArgs.parse_args()
        conversation = ConversationModel.query.get(conversationID)
        if conversation is None:
            abort(409, 'conversation does not exist')
        if not UserResource.authenticate(username,password):
            abort(401)
        msg = MessageModel(
            username = username,
            conversationID = conversationID,
            content = args['content']
        )
        db.session.add(msg)
        db.session.flush()
        db.session.commit()
        return msg
    @api.marshal_with(msgFields, code=200)
    def get(self,username,password,conversationID):
        if not UserResource.authenticate(username,password):
            abort(401)
        participants = ParticipantModel.query.filter(ParticipantModel.conversationID == conversationID)
        participant = participants.filter(ParticipantModel.username == username).first()
        if participant is None:
            abort(403)
        msgsQuery = MessageModel.query.filter(MessageModel.conversationID == conversationID)
        msgsQuery = msgsQuery.filter(MessageModel.timeStamp >= participant.joinedDateTime)
        # if args['content'] is not None:
        #     search = "%{}%".format(args['content'])
        #     msgsQuery = msgsQuery.filter(MessageModel.content.like(search))
        return msgsQuery.all()

convFields = api.model(
    'Conversation', 
    {
        'ID': fields.Integer,
        'name': fields.String,
        'admin': fields.String
    }
)
postConvArgs = reqparse.RequestParser(bundle_errors=True)
postConvArgs.add_argument('name',type=str, required=False)
class ConversationResource(Resource):
    @api.marshal_with(convFields,code=201)
    def post(self, username, password):
        args = postConvArgs.parse_args()
        if not UserResource.authenticate(username,password):
            abort(401)
        conversation = ConversationModel(
            name = args['name'],
            admin = username
        )
        db.session.add(conversation)
        db.session.flush()
        db.session.commit()
        participant = ParticipantModel(
            username = username,
            conversationID = conversation.ID
        )
        db.session.add(participant)
        db.session.flush()
        db.session.commit()
        return conversation
    @api.marshal_with(convFields,code=200)
    def get(self, username, password):
        if not UserResource.authenticate(username,password):
            abort(401)
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
postParticipantArgs.add_argument('participant', type=str, required=True)

class ParticipantResource(Resource):
    @api.marshal_with(participantFields, code=201)
    def post(self, username, password, conversationID):
        if not UserResource.authenticate(username,password):
            abort(401)
        args = postParticipantArgs.parse_args()
        conversation = ConversationModel.query.get(conversationID)
        if conversation is None:
            abort(409, 'conversation does not exist')
        if conversation.admin != username:
            abort(403)
        participants = ParticipantModel.query.filter(ParticipantModel.conversationID == conversationID)
        participant = participants.filter(ParticipantModel.username == args['participant']).first()
        if participant is not None:
            abort(409, 'participant already added')
        participant = ParticipantModel(
            username = args['participant'],
            conversationID = conversationID
        )
        db.session.add(participant)
        db.session.flush()
        db.session.commit()
        return participant
    @api.marshal_with(participantFields, code=200)
    def get(self,username,password,conversationID):
        if not UserResource.authenticate(username,password):
            abort(401)
        participants = ParticipantModel.query.filter(ParticipantModel.conversationID == conversationID).all()
        return participants
        

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
postUserArgs.add_argument('role',type=str,required=True)

class UserResource(Resource):
    @api.marshal_with(userFields, code=201)
    def post(self, username, password):
        args = postUserArgs.parse_args()
        user = UserModel.query.filter(UserModel.username == username).first()
        if user is not None:
            abort(409, 'username already exists')
        user = UserModel(
            firstName = args['firstName'],
            lastName = args['lastName'],
            username = username,
            password = password,
            role = args['role']
        )
        db.session.add(user)
        db.session.flush()
        db.session.commit()
        return user
    @api.marshal_with(userFields,code=200)
    def get(self,username,password):
        if not self.authenticate(username,password):
            abort(401)
        user = UserModel.query.filter(UserModel.username == username)
        return user
    def authenticate(username,password):
        user = UserModel.query.filter(UserModel.username == username).first()
        if user is None:
            return False
        if user.password != password:
            return False
        return True

api.add_resource(MsgResource,'/messages/<string:username>/<string:password>/<string:conversationID>')
api.add_resource(ConversationResource,'/conversations/<string:username>/<string:password>')
api.add_resource(ParticipantResource,'/participants/<string:username>/<string:password>/<string:conversationID>')
api.add_resource(UserResource,'/users/<string:username>/<string:password>')

if __name__ == '__main__':
    app.run(debug=True)