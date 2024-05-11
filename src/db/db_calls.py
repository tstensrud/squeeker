import sqlite3
from . import DB_NAME

def fetch_users():
    connect = sqlite3.connect(DB_NAME)
    cursor = connect.cursor()
    result = cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    connect.close()

def new_user(email: str, name: str) -> bool:
    connect = sqlite3.connect(DB_NAME)
    cursor = connect.cursor()
    
    if find_existing_user(email) == 0:
        insert = "INSERT INTO users (email, name) VALUES (?, ?)"
        cursor.execute(insert, (email, name))
        print(f"user added {email}, {name}")
        connect.commit()
        return True
    else:
        print("Email already exists")
        return False
    connect.close()

def find_existing_user(email: str) -> int:
    connect = sqlite3.connect(DB_NAME)
    cursor = connect.cursor()
    cursor.execute("SELECT 1 FROM users WHERE email=?", (email,))
    result = cursor.fetchone()
    print(result)
    connect.close()
    if result != None:
        print("returning 1")
        return 1
    else:
        print("returning 0")
        return 0

def clear_user_table() -> None:
    connect = sqlite3.connect(DB_NAME)
    cursor = connect.cursor()
    cursor.execute("DELETE FROM users")
    connect.commit()
    connect.close()
    print("user-table cleared")
