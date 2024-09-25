import os
from src.bot_data import bot
from data import humidity_queries, temperature_queries
from datetime import datetime

async def send_chart(path, message):
    print("accediendo a imagen")
    file = f"../../{path}"
    if os.path.isfile(file):
        print("imagen encontrada")
        with open(file, "rb") as photo:
            print("imagen")
            await bot.send_photo(message.chat.id, photo)
            os.remove(path=file)
    else:
        print("no se pudo encontrar")


async def h_chart(message):
    data = await humidity_queries.get_from_today()
    print("analizando datos de humedad")

    if data is not None:
        dt = datetime.now()
        path = f"h_{dt.year}_{dt.month}_{dt.day}_{dt.hour}{dt.minute}{dt.second}"
        humidity_queries.get_chart(humidities=data, filename=path)
        return path
    else:
        return None
