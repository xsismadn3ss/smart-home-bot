import os
from src.bot_data import bot
from data import humidity_queries, temperature_queries
from datetime import datetime

async def send_chart(path, message):
    print("accediendo a imagen")
    if os.path.isfile(path):
        print("imagen encontrada")
        with open(path, "rb") as photo:
            print("imagen")
            await bot.send_photo(message.chat.id, photo)
            os.remove(path=path)
    else:
        print("no se pudo encontrar")


async def h_chart(message):
    data = await humidity_queries.get_from_today()
    print("analizando datos de temperatura")

    if data is not None:
        dt = datetime.now()
        path = f"h_{dt.year}_{dt.month}_{dt.day}_{dt.hour}{dt.minute}{dt.second}"
        humidity_queries.get_chart(humidities=data, filename=path)
        return path
    else:
        return None
