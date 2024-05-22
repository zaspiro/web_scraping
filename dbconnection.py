import sqlite3 as s

def create_database(db_name):
    conn = s.connect(db_name)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            code TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def insert_items(db_name, items):
    conn = s.connect(db_name)
    cursor = conn.cursor()
    for name, code in items.items():
        cursor.execute('INSERT INTO items (name, code) VALUES (?, ?)', (name, code))
    conn.commit()
    conn.close()

def display_items(db_name):
    conn = s.connect(db_name)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM items')
    rows = cursor.fetchall()

    for row in rows:
        print(row)
    conn.close()