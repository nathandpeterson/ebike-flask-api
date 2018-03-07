from db import db


class EbikeModel(db.Model):

    __tablename__ = 'ebikes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))
    source = db.Column(db.String(120))

    def __init__(self, name, price, source):
        self.name = name
        self.price = price
        self.source = source

    def json(self):
        return {'name': self.name, 'price': self.price, 'source': self.source}

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
