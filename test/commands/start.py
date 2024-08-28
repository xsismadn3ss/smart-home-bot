from .data import bot

@bot.message_handler(commands=["start"])
def welcome(message):
    print("greeting...")
    bot.reply_to(message, "Hola, bienvenido!!!")