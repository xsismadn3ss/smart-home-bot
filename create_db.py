import sqlite3

conn = sqlite3.connect("bot.db")
cursor = conn.cursor()

sqlcommands: dict = {
    # user
    "User": """CREATE TABLE User ( 
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    chat_id INTEGER NOT NULL UNIQUE
);""",
    # temperature
    "Temperature": """CREATE TABLE Temperature (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    value REAL NOT NULL,
    date DATETIME NOT NULL
);""",
    # humidity
    "Humidity": """CREATE TABLE Humidity (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    value REAL NOT NULL,
    date DATETIME NOT NULL
);""",
    # daily averages
    "Daily_Avergages": """CREATE TABLE Daily_Averages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    avg_temperature REAL NOT NULL,
    avg_humidity REAL NOT NULL,
    date DATE NOT NULL UNIQUE
);""",
}


for command in sqlcommands:
    try:
        cursor.execute(sqlcommands[command])
        print(f"Creating {command}")

    except Exception:
        print(f"{command} is already created")

conn.commit()
conn.close()