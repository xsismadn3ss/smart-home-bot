from datetime import datetime
from sqlite3 import Cursor
from data.functions.db_session import query
import matplotlib.pyplot as plt
from data.models import Humidity


def serialize(mesures: list[tuple] | tuple):
    if mesures is None:
        return None

    data: list[Humidity] = []
    for mesure in mesures:
        data.append(
            Humidity(
                id=mesure[0],
                value=mesure[1],
                date=datetime.fromisoformat(mesure[2]),
            )
        )
    return data


@query
def insert(conn, cursor: Cursor, value):
    sqlcommnad = "INSERT INTO Humidity (value, date) values (?, ?)"
    current_time = datetime.now().isoformat()
    cursor.execute(sqlcommnad, (value, current_time))


@query
def get_all(conn, cursor: Cursor):
    sqlcommand = "SELECT * FROM Humidity"
    cursor.execute(sqlcommand)
    data = cursor.fetchall()
    return serialize(data)


@query
def get_from_today(conn, cursor: Cursor):
    sqlcommand = "SELECT * FROM Humidity WHERE date(date) = date('now')"
    cursor.execute(sqlcommand)
    data = cursor.fetchall()
    return serialize(data)


def get_max(humidities):
    max_humidity = max(humidities, key=lambda t: t.value)
    return max_humidity


def get_chart(humidities: list[Humidity], filename):
    dates = [temp.time for temp in humidities]
    values = [temp.value for temp in humidities]

    plt.figure(figsize=(10, 5))
    plt.plot(dates, values, marker="o", linestyle="-", color="red", label="Humedad")

    plt.xlabel("Hora")
    plt.ylabel("Humedad")
    plt.title("Gráfico de Humedad")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    plt.savefig(filename)
