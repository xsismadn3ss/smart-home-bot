from .data import bot

@bot.message_handler(commands=["start"])
async def welcome(message):
    print("greeting...")
    await bot.reply_to(message, "Hola, bienvenido!!!")