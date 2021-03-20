# Importing sqlalchemy
from flask_sqlalchemy import SQLAlchemy
import datetime

# Instantiating sqlalchemy object
db = SQLAlchemy()


# Creating database class
class Messages(db.Model):
    # Creating field/columns of the database as class variables
    id = db.Column(db.Integer, primary_key=True)

    sender = db.Column(db.String(30), unique=False, nullable=False)
    receiver = db.Column(db.String(30), unique=False, nullable=False)
    subject = db.Column(db.String(200), unique=False, nullable=False)
    message = db.Column(db.String(500), unique=False, nullable=False)
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    status = db.Column(db.String(10), unique=False, nullable=False)

    def __init__(self, sender, receiver, subject, message):
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.message = message
        self.status = "unread"

        # Method to show data as dictionary object

    def json(self):
        return {'Sender': self.sender, 'Receiver': self.receiver, 'Subject': self.subject, 'Message': self.message, 'Created': str(self.created), 'Status': self.status}

        # Method to find the query message is existing or not

    @classmethod
    def get_messages_by_sender(cls, sender):
        return cls.query.filter_by(sender=sender).all()

    @classmethod
    def get_specific_message(cls, subject, role, name):
        print("calls the function")

        if role == "sender":
            return cls.query.filter_by(sender=name, subject=subject).first()
        else:
            return cls.query.filter_by(receiver=name, subject=subject).first()

    @classmethod
    def get_message_by_subject(cls, subject):
        message = cls.query.filter_by(subject=subject).first()
        message.status = "read"
        db.session.commit()

        return message.json()

    @classmethod
    def get_unread_messages(cls, status):
        return cls.query.filter_by(status=status).all()

    # Method to save data to database
    def save_to(self):
        db.session.add(self)
        db.session.commit()

    # Method to delete data from database
    def delete_(self):
        db.session.delete(self)
        db.session.commit()
