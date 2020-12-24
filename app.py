from flask import Flask
from flask_restful import Resource, Api, request, reqparse
import sqlite3
from models.user import UserModel


app = Flask(__name__)
api = Api(app)

class User_List(Resource):
    def get(self):
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        results = c.execute("SELECT * FROM users")
        items = []
        for result in results:
          items.append({'id': result[0], 'name': result[1], 'username': result[2], 'email': result[3]})
        conn.close()
        return {'users': items }, 200
        


class User(Resource):
    def get(self, username):
      user = UserModel.find_by_username(username)
      if user:
        return UserModel(*user).to_dict(), 200
      return {'msg': 'user not found'}, 404
    
    def post(self, username):
      parser = reqparse.RequestParser()
      parser.add_argument('name', required=True)
      parser.add_argument('email', required=True)
      parser.add_argument('password', required=True)
      req = parser.parse_args()
      user_exists = UserModel.find_by_username(username)
      if user_exists:
        return {'msg': f"user with username '{username}' already exists"}, 409
      else:
        user = UserModel(req['name'], username, req['email'], req['password'])
        user.insert()
        return user.to_dict(), 201

    def put(self, username):
      user_exists = UserModel.find_by_username(username)

      
      if user_exists:
        req = request.get_json()
        updated_model = {'name': user_exists[0], 'email': user_exists[2], 'password': user_exists[3]}
        updated_model.update(req)
        return UserModel.update(username, updated_model['name'], updated_model['email'], updated_model['password']).to_dict(), 200
      else:
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True)
        parser.add_argument('email', required=True)
        parser.add_argument('password', required=True)
        req = parser.parse_args()

        user = UserModel(req['name'], username, req['email'], req['password'])
        UserModel.insert(user)
        return user.to_dict(), 201


    

api.add_resource(User_List, '/users')
api.add_resource(User, '/user/<string:username>')

app.run(port=5000, debug=True)