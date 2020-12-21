import sqlite3
# DATABASE INIT AND MOCK DATA, run once

users = [
  {
    "name": "Leanne Graham",
    "username": "Bret",
    "email": "Sincere@april.biz",
    "pwd": "543"
  },
  {
    "name": "Ervin Howell",
    "username": "Antonette",
    "email": "Shanna@melissa.tv",
    "pwd": "253"
  },
  {
    "name": "Clementine Bauch",
    "username": "Samantha",
    "email": "Nathan@yesenia.net",
    "pwd": "1154"
  },
  {
    "name": "Patricia Lebsack",
    "username": "Karianne",
    "email": "Julianne.OConner@kory.org",
    "pwd": "testpw"
  },
  {
    "name": "Chelsey Dietrich",
    "username": "Kamren",
    "email": "Lucio_Hettinger@annie.ca",
    "pwd": "543cxL"
  },
  {
    "name": "Mrs. Dennis Schulist",
    "username": "Leopoldo_Corkery",
    "email": "Karley_Dach@jasper.info",
    "pwd": "77gv4C"
  },
  {
    "name": "Kurtis Weissnat",
    "username": "Elwyn.Skiles",
    "email": "Telly.Hoeger@billy.biz",
    "pwd": "Cx54S3"
  },
  {
    "name": "Nicholas Runolfsdottir V",
    "username": "Maxime_Nienow",
    "email": "Sherwood@rosamond.me",
    "pwd": "XXsk7cD2"
  },
  {
    "name": "Glenna Reichert",
    "username": "Delphine",
    "email": "Chaim_McDermott@dana.io",
    "pwd": "5Wq42"
  },
  {
    "name": "Clementina DuBuque",
    "username": "Moriah.Stanton",
    "email": "Rey.Padberg@karina.biz",
    "pwd": "99Lo4Z2"
  }
]

conn = sqlite3.connect('data.db')
c = conn.cursor()

c.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name text, username text, email text, pwd text)")
conn.commit()
query = "INSERT INTO users VALUES (NULL, ?, ?, ?, ?)"
for usr in users:
  c.execute(query, (usr['name'], usr['username'], usr['email'], usr['pwd']))

conn.commit()
result = c.execute("SELECT * FROM users")
for r in result:
  print(r)
  
conn.close()

