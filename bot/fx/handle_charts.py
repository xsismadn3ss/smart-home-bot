import os
from bot.bot_data import bot
from data import humidity_queries, temperature_queries
from datetime import datetime

async def send_chart(path, message):
    print("accediendo a imagen")

    with open(path, "rb") as photo:
        print("enviando imagen")
        await bot.send_photo(message.chat.id, photo)
        os.remove(path=path)

def create_path(title):
    dt = datetime.now()
    path = f"{title}_{dt.year}_{dt.month}_{dt.day}_{dt.hour}{dt.minute}{dt.second}.png"
    return path

async def h_chart():
    data = await humidity_queries.get_from_today()
    print("analizando datos de humedad")

    if data is not None:
        path = create_path("h")
        humidity_queries.get_chart(humidities=data, filename=path)
        return path
    else:
        return None

async def t_chart():
    data = await temperature_queries.get_from_today()
    print("analizando datos de temperatura")

    if data is not None:
        path = create_path("t")
        temperature_queries.get_chart(temperatures=data, filename=path)
        return path
    else:
        return None