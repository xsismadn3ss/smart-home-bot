from .data import bot


@bot.message_handler(commands=["hour"])
async def send_time(message):
    import datetime

    now = datetime.datetime.now()
    print("sending time")
    await bot.reply_to(message, f"Son las {now.hour}:{now.minute}")
