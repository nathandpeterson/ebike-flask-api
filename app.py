import os
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

from resources.ebike import Ebike, EbikeList
from resources.user import User, UserList
from resources.user_ebike import UserEbikes

app = Flask(__name__)
CORS(app)

app.secret_key = 'secret'

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(Ebike, '/ebike/<string:name>')
api.add_resource(EbikeList, '/ebikes')
api.add_resource(UserEbikes, '/user/<string:email>/ebikes')
api.add_resource(User, '/user/<string:email>')
api.add_resource(UserList, '/users')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
