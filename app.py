from flask import Flask
from flask_restful import Resource, Api

#mock data until sqlite
from mock_data import users

app = Flask(__name__)
api = Api(app)

class User_List(Resource):
    def get(self):
        return {'users': users}, 200

class User(Resource):
    def get(self, id):
        user = next(filter(lambda x: x['id'] == id, users), None)
        if user:
          return (user, 200)
        return (None, 404)

api.add_resource(User_List, '/users')
api.add_resource(User, '/user/<int:id>')

app.run(port=5000, debug=True)