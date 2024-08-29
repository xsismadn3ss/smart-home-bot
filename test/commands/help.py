from .data import bot
@bot.message_handler(commands=["help"])
def help(message):
    print("sending description...")
    bot.reply_to(
        message,
        "Este es un bot de prueba hecho en telegram\n\nLista de comandos:\n-/help - Descripción del bot",
    )