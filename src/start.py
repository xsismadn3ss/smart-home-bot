from .bot_data import bot

@bot.message_handler(commands=["start"])
async def welcome(message):
    print("Greeting")
    await bot.reply_to(message,"Bienvenido")