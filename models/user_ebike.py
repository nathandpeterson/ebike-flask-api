from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSON
from db import db


class UserEbikeModel(db.Model):
    
    __tablename__ = 'user_ebike'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    ebike_id = db.Column(db.Integer, db.ForeignKey('ebikes.id'))

    def json(self):
        return {'user_id': self.user_id, 'ebike_id': self.ebike_id}

    def __init__(self, user_id, ebike_id):
        self.user_id = user_id
        self.ebike_id = ebike_id

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()