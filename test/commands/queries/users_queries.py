from .connection import get_db_connection

async def get_users():
    conn = get_db_connection()
    cursor = conn.cursor()
    sqlcommand = "select * from Users"
    cursor.execute(sqlcommand)
    data = cursor.fetchall()
    conn.close()
    return data


async def save_id(value:str):
    conn = get_db_connection()
    cursor = conn.cursor()
    sqlcommand = f"INSERT INTO Users (chat_id) values ('{value}')"
    cursor.execute(sqlcommand)
    conn.commit()
    conn.close()
