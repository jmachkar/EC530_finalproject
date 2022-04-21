from flask import Flask, Response, abort
from flask_restx import Api, Resource, reqparse, fields
from models import db, MessageModel

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chatDatabase.db'


msgFields = api.model('Message',
    {
        'msgID' = fields.String,
        'senderID' = fields.Integer,
        'conversationID' = fields.Integer,
        'content' = fields.String,
        'timeStamp' = fields.DateTime
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
        return 201
    @api.marshal_with(msgFields, code=200)
    def get(self):
        args = getMsgArgs.parse_args()
        msgs = MessageModel.query.all()
        if args['senderID'] is not None:
            msgs = msgs.filter_by(MessageModel.senderID == args['senderID'])
        if args['conversationID'] is not None:
            msgs = msgs.filter_by(MessageModel.conversationID == args['conversationID'])
        if args['content'] is not None:
            search = "%{}%".format(args['content'])
            msgs = msgs.filter_by(MessageModel.content.like(search))
        return msgs.all(), 200
    


    


