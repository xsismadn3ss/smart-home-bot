from datetime import datetime
from .bot_data import bot
from data import humidity_queries, temperature_queries


@bot.message_handler(commands=["reports"])
async def reports(message):
    today_h = await humidity_queries.get_from_today()
    dt = datetime.now()
    path = f"assets/{dt.year}_{dt.month}_{dt.day}_{dt.hour}{dt.minute}{dt.second}"
    humidity_queries.get_chart(humidities=today_h, filename=path)
    await bot.send_photo()
