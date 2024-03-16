from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime

class Server(db.Model):
    __tablename__ = 'servers'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    server_name = db.Column(db.String, nullable=False)
    img_url = db.Column(db.String, nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # relationships
    server_owner = db.relationship("User", back_populates="user_server")


    def to_dict(self):
        return {
            'id': self.id,
            'server_name': self.server_name,
            'img_url': self.img_url,
            'owner_id': self.owner_id,
            'created_at': self.created_at
        }
