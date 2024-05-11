import sqlite3
from . import DB_NAME


def delete_table(name):
    connect = sqlite3.connect(DB_NAME)
    cursor = connect.cursor()
    cursor.execute(f"DROP TABLE IF EXISTS {name}")
    connect.commit()
    connect.close()

def create_user_table():
    connect = sqlite3.connect(DB_NAME)
    cursor = connect.cursor()
    cursor.execute("CREATE TABLE users(id INTEGER PRIMARY KEY AUTOINCREMENT, email TEXT NOT NULL, name TEXT NOT NULL)")
    connect.commit()
    connect.close()
    print("Table created")