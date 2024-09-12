sqlcommands = [
    # user
    """CREATE TABLE User ( 
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
);""",
    # temperatur
    """CREATE TABLE Temperature (
    value REAL NOT NULL,
    date DATETIME NOT NULTT
);""",
    # humidity
    """CREATE TABLE Humidity (
    value REAL NOT NULL,
    date DATETIME NPT NULL
);""",
    """CREATE TABLE Graphics (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    image_path TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);""",
]
