from flask_restful import Resource, reqparse
from models.ebike import EbikeModel

class Ebike(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help="This field cannot be left blank")
    parser.add_argument('source',
                        required=True,
                        help="This field cannot be left blank")

    def get(self, name):
        ebike = EbikeModel.find_by_name(name)
        if ebike:
            return ebike.json()
        return {'message': 'ebike not found'}, 404

    def post(self, name):
        if EbikeModel.find_by_name(name):
            return {'message': 'An ebike with name {} already exists.'.format(name)}, 400

        data = Ebike.parser.parse_args()

        ebike = EbikeModel(name, **data)
        try:
            ebike.save_to_db()
        except:
            return {'message': 'an error occurred'}, 500

        return ebike.json(), 201

    def delete(self, name):
        ebike =  EbikeModel.find_by_name(name)
        if ebike:
            ebike.delete_from_db()
        return {'message': 'item has been deleted'}
    
    def put(self, name):
        data = Ebike.parser.parse_args()

        ebike = EbikeModel.find_by_name(name)

        if ebike == None:
            ebike = EbikeModel(name, **data)
        else:
            ebike.price = data['price']

        ebike.save_to_db()

        return ebike.json()

class EbikeList(Resource):
    def get(self):
        return {'ebikes': list(map(lambda x: x.json(), EbikeModel.query.all())) }
   
