from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required
from security import authenticate, identity

app = Flask(__name__)
app.secret_key = "wolf"
api = Api(app)

jwt = JWT(app, authenticate, identity)

items = []

class Item(Resource):
    @jwt_required
    def get(self, name):
        items = next(filter(lambda x: x['name'] == name, items), None) #returns 1st match
        return {'item' : item}, 200 if item else 404

    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None)is not None: #test to see if already
                return {'message' : f('An item the name "{name}" already exists')}, 400
        data = request.get_json()
        item = {'name': name, 'price': data["price"]}
        items.append(item)
        return item, 201

    def delete(self, name):
        pass

    def put(self, name):
        pass


class ItemList(Resource):
    def get(self):
        return {"items" : items}


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

app.run(port=5000, debug=True)