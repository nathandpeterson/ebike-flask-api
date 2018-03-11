from flask_restful import Resource, reqparse
from models.ebike import EbikeModel
from models.user import UserModel
from db import db


class UserEbikes(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('ebike_id',
                        type=int,
                        required=True,
                        help="This field cannot be left blank")

    def get(self, email):
        user = UserModel.find_by_email(email)
        ebikes = user.ebikes
        json = list(map(lambda x: x.json(), ebikes))
        return {'ebikes': json}

    def post(self, email):
        data = UserEbikes.parser.parse_args()
        user = UserModel.find_by_email(email)
        if not user:
            return {'message': 'no such user'}, 404
        ebike = EbikeModel.find_by_id(data['ebike_id'])
        try:
            user.ebikes.append(ebike)
            db.session.commit()
        except SystemError:
            return {'message': 'something went wrong'}, 500
        return {'message': 'ebike added to user'}