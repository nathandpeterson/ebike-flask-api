from flask_restful import Resource, reqparse
from models.user_ebike import UserEbikeModel
from models.user import UserModel


class UserEbikes(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('ebike_id',
                        type=int,
                        required=True,
                        help="This field cannot be left blank")

    def get(self, email):
        # Method should get all ebikes for a user
        return {'this is you?': email}

    def post(self, email):
        data = UserEbikes.parser.parse_args()
        user_data = UserModel.find_by_email(email).json()
        if not user_data:
            return {'message': 'no such user'}, 404
        user_id = user_data['id']
        user_ebike_data = UserEbikeModel(user_id, data['ebike_id'])
        try:
            user_ebike_data.save_to_db()
        except EnvironmentError:
            return {'message': 'something went wrong'}, 500
        return {'message': 'success'}