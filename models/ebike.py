from db import db
from models.user import user_bike


class EbikeModel(db.Model):

    __tablename__ = 'ebikes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    brand = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))
    source_url = db.Column(db.String(120))
    img_url = db.Column(db.String(120))
    users = db.relationship('UserModel', secondary=user_bike, back_populates='ebikes')

    def __init__(self, name, price, brand, img_url, source_url):
        self.name = name
        self.price = price
        self.brand = brand
        self.img_url = img_url
        self.source_url = source_url

    def json(self):
        return {'name': self.name, 
        'price': self.price, 
        'brand': self.brand, 
        'source_url': self.source_url,
        'img_url': self.img_url}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
