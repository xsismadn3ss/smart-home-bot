import sqlite3

conn = sqlite3.connect("telebot.db")
cursor = conn.cursor()

sqlcommands = [
"""
CREATE TABLE Earn (
id INTEGER PRIMARY KEY AUTOINCREMENT,
datetime DATETIME NOT NULL,
value TEXT NOT NULL, reason TEXT);
""",
"""
CREATE TABLE Graphics (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    datetime DATETIME NOT NULL,
    image BLOB
);""",
"""
CREATE TABLE Spent (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    datetime DATETIME NOT NULL,
    value TEXT NOT NULL
, "reason" TEXT)
""",
"""
CREATE TABLE "Users" (
	"id"	INTEGER,
	"chat_id"	TEXT NOT NULL UNIQUE,
	PRIMARY KEY("id" AUTOINCREMENT)
)
""",
]

for command in sqlcommands:
    cursor.execute(command)
    conn.commit()
conn.close()
