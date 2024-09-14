import sqlite3

conn = sqlite3.connect('bot.db')
cursor = conn.cursor()

sqlcommands = [
    # user
    """CREATE TABLE User ( 
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
);""",
    # temperatur
    """CREATE TABLE Temperature (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    value REAL NOT NULL,
    date DATETIME NOT NULL
);""",
    # humidity
    """CREATE TABLE Humidity (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    value REAL NOT NULL,
    date DATETIME NOT NULL
);""",
    #graphics
    """CREATE TABLE Graphics (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    image_path TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);""",
]

for command in sqlcommands:
    cursor.execute(command)
conn.commit()
conn.close()