from datetime import datetime
from sqlite3 import Cursor
from data.functions.db_session import query
import matplotlib.pyplot as plt
from data.models import Temperature


def serialize(mesures: list[tuple] | tuple):
    if mesures is None:
        return None

    data: list[Temperature] = []
    for mesure in mesures:
        data.append(
            Temperature(
                id=mesure[0],
                value=mesure[1],
                date=datetime.fromisoformat(mesure[2]),
            )
        )
    return data


@query
def insert(conn, cursor: Cursor, value):
    sqlcommnad = "INSERT INTO Temperature (value, date) values (?, ?)"
    current_time = datetime.now().isoformat()
    cursor.execute(sqlcommnad, (value, current_time))


@query
def get_all(conn, cursor: Cursor):
    sqlcommand = "SELECT * FROM Temperature"
    cursor.execute(sqlcommand)
    data = cursor.fetchall()
    return serialize(data)


@query
def get_from_today(conn, cursor: Cursor):
    sqlcommand = "SELECT * FROM Temperature WHERE date(date) = date('now')"
    cursor.execute(sqlcommand)
    data = cursor.fetchall()
    return serialize(data)


def get_max(temperatures):
    max_temperature = max(temperatures, key=lambda t: t.value)
    return max_temperature


def get_chart(temperatures: list[Temperature], filename):
    dates = [temp.time for temp in temperatures]
    values = [temp.value for temp in temperatures]

    plt.figure(figsize=(10, 5))
    plt.plot(dates, values, marker="o", linestyle="-", color="red", label="Temperatura")

    plt.xlabel("Hora")
    plt.ylabel("Temperatura")
    plt.title("Gráfico de temperatura")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    plt.savefig(filename)
