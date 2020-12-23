import sqlite3

class UserModel:
    def __init__(self, name, username, email, pwd):
        self.name = name
        self.username = username
        self.email = email
        self.pwd = pwd
    
    def to_dict(self):
        return {'name': self.name, 'username': self.username, 'email': self.email}

    def insert(self):
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        query = "INSERT INTO users VALUES (NULL, ?, ?, ?, ?)"
        c.execute(query, (self.name, self.username, self.email, self.pwd))
        conn.commit()
        c.close()


    @classmethod
    def find_by_username(cls, username):
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
      
        query = "SELECT name, username, email FROM users WHERE username=?"
        user = c.execute(query, (username, )).fetchone()
        conn.close()
        return user



