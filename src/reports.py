from datetime import datetime
from .bot_data import bot
from data import humidity_queries, temperature_queries


@bot.message_handler(commands=["reports"])
async def reports(message):
    today_h = humidity_queries.get_from_today()
    dt = datetime.now()
    path = "assets/{}_{}_{}_{}{}{}".format(
        dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second
    )
    humidity_queries.get_chart()
    await bot.reply_to(message, "Generando graficas")
