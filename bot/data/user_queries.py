from data.functions.db_session import query
from data.models import User
from aiosqlite import Connection, Cursor


def serialize(users):
    if users is None:
        return None

    elif type(users) == list:
        data: list[User] = []
        for user in users:
            data.append(User(id=user[0], chat_id=user[1]))
        return data

    return User(id=users[0], chat_id=users[1])


@query
async def insert(conn: Connection, cursor: Cursor, chat_id):
    sql_command = "INSERT INTO User(chat_id) values (?)"
    await cursor.execute(sql_command, (chat_id,))


@query
async def get_all(conn: Connection, cursor: Cursor):
    sql_command = "SELECT * FROM User"
    await cursor.execute(sql_command)
    data = await cursor.fetchall()
    return serialize(data)


@query
async def get(conn: Connection, cursor: Cursor, chat_id):
    sql_command = "SELECT * FROM User WHERE chat_id = ?"
    await cursor.execute(sql_command, (chat_id,))
    data = await cursor.fetchone()
    return serialize(data)
