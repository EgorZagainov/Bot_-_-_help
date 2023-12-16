import sqlite3 as sq


db = sq.connect('db/db3')
cur = db.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_name TEXT NOT NULL,
        user_id INTEGER
    );""")

db.commit()

db.close()