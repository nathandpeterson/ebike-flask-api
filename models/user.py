from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSON
from db import db
from models.user_ebike import UserEbikeModel

class UserModel(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    password = db.Column(db.String(80))
    email = db.Column(db.String(80))

    def __init__(self, email, first_name, last_name, password):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
    
    def json(self):
        return {'id': self.id,
                'first_name': self.first_name,
                'last_name': self.last_name,
                'password': self.password,
                'email': self.email}
    
    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()