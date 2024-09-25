from data.functions.db_session import query
from data.models import User
from sqlite3 import Connection, Cursor


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
def insert(conn: Connection, cursor: Cursor, chat_id):
    sql_command = "INSERT INTO User(chat_id) values (?)"
    cursor.execute(sql_command, (chat_id,))


@query
def get_all(conn: Connection, cursor: Cursor):
    sql_command = "SELECT * FROM User"
    cursor.execute(sql_command)
    data = cursor.fetchall()
    return serialize(data)


@query
def get(conn: Connection, cursor: Cursor, chat_id):
    sql_command = "SELECT * FROM User WHERE chat_id = ?"
    cursor.execute(sql_command, (chat_id,))
    data = cursor.fetchone()
    return serialize(data)
