import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_jwt import JWT

# from resources.ebike import Ebike

app = Flask(__name__)

app.secret_key = 'secret'

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

api = Api(app)

@app.route('/')
def hello():
    return 'Hello World!'

@app.before_first_request
def create_tables():
    db.create_all()

# api.add_resource(Ebike, '/ebike/<string:name>')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
