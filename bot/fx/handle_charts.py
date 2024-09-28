from os import remove
from bot.bot_data import bot
from data import humidity_queries, temperature_queries
from datetime import datetime

async def send_chart(path, chat_id):
    print("accediendo a imagen")

    with open(path, "rb") as photo:
        print("enviando imagen")
        await bot.send_photo(chat_id, photo)
        remove(path=path)

def create_path(title):
    dt = datetime.now()
    path = f"{title}_{dt.year}_{dt.month}_{dt.day}_{dt.hour}{dt.minute}{dt.second}.png"
    return path

async def h_chart(humidities):
    data = humidities
    print("analizando datos de humedad")

    if data is not None:
        path = create_path("h")
        humidity_queries.get_chart(humidities=data, filename=path)
        return path
    else:
        return None

async def t_chart(temperatures):
    data = temperatures
    print("analizando datos de temperatura")

    if data is not None:
        path = create_path("t")
        temperature_queries.get_chart(temperatures=data, filename=path)
        return path
    else:
        return None