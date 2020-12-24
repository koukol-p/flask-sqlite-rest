import sqlite3

class UserModel:
    def __init__(self, name, username, email, password):
        self.name = name
        self.username = username
        self.email = email
        self.password = password
    
    def to_dict(self):
        return {'name': self.name, 'username': self.username, 'email': self.email}

    def insert(self):
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        query = "INSERT INTO users VALUES (NULL, ?, ?, ?, ?)"
        c.execute(query, (self.name, self.username, self.email, self.password))
        conn.commit()
        conn.close()

    @classmethod
    def update(cls, username, name, email, password):
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        query = "UPDATE users SET name=?, email=?, pwd=? WHERE username=?"
        c.execute(query, (name, email, password, username))
        conn.commit()
        conn.close()
        return cls(name, username, email, password)


    @classmethod
    def find_by_username(cls, username):
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
      
        query = "SELECT name, username, email, pwd FROM users WHERE username=?"
        user = c.execute(query, (username, )).fetchone()
        conn.close()
        return user



