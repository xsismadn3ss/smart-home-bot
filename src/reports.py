from .bot_data import bot


@bot.message_handler(commands=["reports"])
async def reports(message):
    print("Generando Grafica...")
    await bot.reply_to(message,"soy una grafica.com")