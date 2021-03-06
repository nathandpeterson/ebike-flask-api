from flask_restful import Resource, reqparse
from models.user import UserModel


class User(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('first_name',
                        required=True,
                        help="This field cannot be left blank")
    parser.add_argument('last_name',
                        required=True,
                        help="This field cannot be left blank")
    parser.add_argument('password',
                        required=True,
                        help="This field cannot be left blank")

    def get(self, email):
        user = UserModel.find_by_email(email)
        if user:
            return user.json()
        return {'message': 'user not found'}, 404

    def post(self, email):
        if UserModel.find_by_email(email):
            return {'message': 'That email is taken'}, 400
        data = User.parser.parse_args()
        user = UserModel(email, data['first_name'], data['last_name'], data['password'])
        try:
            user.save_to_db()
        except SystemError:
            return {'message': 'something went wrong'}, 500
        return {'message': 'Account created for ' + data['first_name']}, 201


class UserList(Resource):
    # Fetch a list of users, for development purposes or admin access only.
    def get(self):
        return {'users': list(map(lambda x: x.json(), UserModel.query.all()))}
