import sqlite3


def get_conection():
    path = "bot.db"
    conn = sqlite3.connect(path)
    return conn


def query(func):
    def wrapper(*args, **kwargs):
        print("Executing query")
        conn = get_conection()
        cursor = conn.cursor()
        try:
            result = func(conn, cursor, *args, **kwargs)
            conn.commit()

        except Exception as e:
            conn.rollback()
            raise e
        finally:
            conn.close()
        return result

    return wrapper
