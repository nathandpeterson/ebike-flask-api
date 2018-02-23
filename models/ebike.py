from db import db

class EbikeModel(db.Model):

    __tablename__ = 'ebikes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def json(self):
        return {'name': self.name, 'price': self.price}

    @classmethod
    def find_by_name(cls, name):
        # select * from tablename where name = name
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        # 'INSERT INTO items VALUES(?,?)'
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        # UPDATE items SET price=? WHERE name=?
        db.session.delete(self)
        db.session.commit()
