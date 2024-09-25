from sqlite3 import Cursor
from data.functions.db_session import query


@query
async def daily_average(conn, cursor: Cursor):
    sqlcommand = """
        INSERT INTO Daily_Averages (avg_temperature, avg_humidity, date)
        SELECT AVG(T.value) AS avg_temperature, AVG(H.value) AS avg_humidity,
        DATE(T.date) AS date FROM Temperature T JOIN Humidity H
        ON DATE(T.date) = DATE(H.date) GROUP BY DATE(T.date);
    """
    await cursor.execute()


@query
async def weekly_average(conn, cursor: Cursor):
    sqlcommnad = """
        INSERT INTO Weekly_Averages (avg_temperature, avg_humidity, week_start_date)
        SELECT AVG(T.value) AS avg_temperature, AVG(H.value) AS avg_humidity,
        DATE(T.date, 'weekday 0', '-6 days') AS week_start_date  -- Start date of the week (Monday)
        FROM  Temperature T JOIN Humidity H
        ON  DATE(T.date) = DATE(H.date) GROUP BY DATE(T.date, 'weekday 0', '-6 days');  -- Group by week
    """
    await cursor.execute()
