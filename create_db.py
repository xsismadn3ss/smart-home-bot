sqlcommands = [
    """CREATE TABLE User (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
);""",
    """CREATE TABLE Temperature (
    value REAL NOT NULL,
    date DATETIME NOT NULTT
);""",
    """CREATE TABLE Humidity (
    value REAL NOT NULL,
    date DATETIME NPT NULL
);""",
]
