from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime

class Channel(db.Model):
    __tablename__ = 'channels'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    channel_name = db.Column(db.String, nullable=False)
    server_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("server.id")), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # relationships
    channel_server = db.relationship("Server", back_populates="server_channel")


    def to_dict(self):
        return {
            'id': self.id,
            'channel_name': self.channel_name,
            'server_id': self.owner_id,
            'created_at': self.created_at
        }
