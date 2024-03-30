from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime

class channel_messages(db.Model):
    __tablename__ = 'channels_messages'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String, nullable=False)
    attatchment_url = db.Column(db.String, nullable=False)
    channel_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("channels.id")), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # relationships
    channel_owner = db.relationship("User", back_populates="user_channel")


    def to_dict(self):
        return {
            'id': self.id,
            'channel_name': self.channel_name,
            'img_url': self.img_url,
            'owner_id': self.owner_id,
            'created_at': self.created_at
        }
