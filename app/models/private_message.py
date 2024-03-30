from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime

class Private_Message(db.Model):
    __tablename__ = 'private_messages'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String, nullable=False)
    attatchment_url = db.Column(db.String)
    sender_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")), nullable=False)
    recipient_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # relationships
    private_message_sender = db.relationship("User", back_populates="sender_private_message")
    private_message_recipient = db.relationship("User", back_populates="recipient_private_message")


    def to_dict(self):
        return {
            'id': self.id,
            'message': self.message,
            'attatchment_url': self.attatchment,
            'sender_id': self.sender_id,
            'recipient_id': self.recipient_id,
            'created_at': self.created_at
        }
