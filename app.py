# base.py
# Import necessary packages
from flask import Flask
from flask_restful import Resource, reqparse, Api

# Instantiate a flask object
app = Flask(__name__)
# Instantiate Api object
api = Api(app)
# Setting the location for the sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///base.db'
# Adding the configurations for the database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config["DEBUG"] = True
# Import necessary classes from base.py
from base import Messages, db

# Link the app object to the Messages database
db.init_app(app)
app.app_context().push()
# Create the databases
db.create_all()


# Creating a class to create get, post, put & delete methods
class Messages_List(Resource):
    # Instantiating a parser object to hold data from message payload
    parser = reqparse.RequestParser()
    parser.add_argument('receiver', type=str, required=False, help='Receiver of the message')
    parser.add_argument('subject', type=str, required=False, help='Subject of the message')
    parser.add_argument('message', type=str, required=True, help='Message')

    # Creating the get method
    def get(self, sender):
        items = Messages.get_messages_by_sender(sender)
        if items:
            return {'Messages': list(map(lambda x: x.json(), items))}
        return {'Messages': 'Messages were not found'}

    # Creating the post method
    def post(self, sender):
        args = Messages_List.parser.parse_args()
        item = Messages(sender, args['receiver'], args['subject'], args['message'])

        item.save_to()
        return item.json()


# Creating a class to get all the messages from the database.
class All_Messages(Resource):
    # Defining the get method
    def get(self):
        return {'Messages': list(map(lambda x: x.json(), Messages.query.all()))}
    # Adding the URIs to the api


class Delete_Message(Resource):
    # Defining the delete method

    parser = reqparse.RequestParser()
    parser.add_argument('subject', type=str, required=False, help='Subject of the message')
    parser.add_argument('role', type=str, required=True, help='Role')

    # Creating the delete method
    def delete(self, name):
        args = Delete_Message.parser.parse_args()
        item = Messages.get_specific_message(args['subject'], args['role'], name)
        if item:
            item.delete_()
            return {'Message': 'with the subject {} has been deleted from records'.format(args['subject'])}
        return {'Message': 'with the subject {} is already not on the list'.format(args['subject'])}


class Read_Message(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('subject', type=str, required=False, help='Subject of the message')

    def get(self):
        args = Read_Message.parser.parse_args()
        item = Messages.get_message_by_subject(args['subject'])
        if item:
            return {'Message': '{}'.format(item["Message"])}
        else:
            return {'Message': 'with the subject {} was not found'.format(args['subject'])}


class Unread_Messages(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('status', type=str, required=False, help='Status of the message')

    def get(self):
        args = Unread_Messages.parser.parse_args()
        print(args['status'])
        items = Messages.get_unread_messages(args['status'])
        if items:
            return {'Messages': list(map(lambda x: x.json(), items))}
        else:
            return {'All messages are read'}


api.add_resource(All_Messages, '/')
api.add_resource(Messages_List, '/<string:sender>')
api.add_resource(Delete_Message, '/<string:name>')
api.add_resource(Read_Message, '/single-message')
api.add_resource(Unread_Messages, '/unread-messages/')
if __name__ == '__main__':
    # Run the applications
    app.run()
