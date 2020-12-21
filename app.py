from flask import Flask
from flask_restful import Resource, Api
import sqlite3

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
      conn = sqlite3.connect('data.db')
      c = conn.cursor()
      query = "SELECT id, name, username, email FROM users WHERE username=?"
      result = c.execute(query, (username, ))
      user = result.fetchone()
      conn.close()
      if user:
        return {'user': {'id': user[0], 'name': user[1], 'username': user[2], 'email': user[3]}}, 200
      return {'msg': 'user not found'}
      
        

api.add_resource(User_List, '/users')
api.add_resource(User, '/user/<string:username>')

app.run(port=5000, debug=True)