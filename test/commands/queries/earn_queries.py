import sqlite3
import datetime


def get_db_connection():
    conn = sqlite3.connect("telebot.db")
    return conn


async def insert(value: str) -> bool:
    conn = get_db_connection()
    cursor = conn.cursor()
    data = value.split('|')
    formatted_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        sqlcommand = (
            f"INSERT INTO Earn (datetime, value, reason) VALUES ('{formatted_date}', '${data[0]}', '{data[1]}')"
        )
        cursor.execute(sqlcommand)
        conn.commit()
    except Exception as e:
        print(f"Error inserting data: {e}")
        return False

    conn.close()
    return True


async def get_all():
    conn = get_db_connection()
    cursor = conn.cursor()
    sqlcommand = f"SELECT * FROM Earn"
    cursor.execute(sqlcommand)
    data = cursor.fetchall()
    conn.close()
    return data
