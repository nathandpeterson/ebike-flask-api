from flask_restful import Resource, reqparse
from models.user_ebike import UserEbikeModel
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
        # This query is returning an error, still working on it.
        x = user.query.filter(user.wishlist.any()).all()
        return {'user': ''}

    def post(self, email):
        data = UserEbikes.parser.parse_args()
        user = UserModel.find_by_email(email)
        if not user:
            return {'message': 'no such user'}, 404
        ebike = EbikeModel.find_by_id(data['ebike_id'])
        try:
            user.wishlist.append(ebike)
            db.session.commit()
        except SystemError:
            return {'message': 'something went wrong'}, 500
        return {'message': 'success'}