import sqlite3
from .common_fx.wrap_input import wrap_input
from .common_fx.current_time import current_time
from .connection import get_db_connection

async def insert(value:str) -> bool:
    conn = get_db_connection()
    cursor = conn.cursor()

    data = wrap_input(value)
    date = current_time()

    try:
        sqlcommand = f"INSERT INTO Spent (datetime, value, reason) VALUES ('{date}', '${data[0]}', '{data[1]}')"
        cursor.execute(sqlcommand)
        conn.commit()
    except Exception as e:
        print(f'Error inserting data: {e}')
        return False
    finally:
        conn.close()

    return True


async def get_all():
    conn = get_db_connection()
    cursor = conn.cursor()
    sqlcommand = f"SELECT * FROM Spent"
    cursor.execute(sqlcommand)
    data = cursor.fetchall()
    conn.close()
    return data
