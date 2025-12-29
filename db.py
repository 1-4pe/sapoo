import sqlite3

DATEBASE = 'database.db'

def create_books_table():
    con = sqlite3.connect(DATEBASE)
    con.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            price INTEGER,
            arrival_day TEXT
        )
    """)
    con.close()
