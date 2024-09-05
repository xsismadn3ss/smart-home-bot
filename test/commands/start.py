from .data import bot
from .queries.users_queries import save_id

@bot.message_handler(commands=["start"])
async def welcome(message):
    print("greeting...")
    await save_id(message.chat.id)
    print("id guardado con exito")
    await bot.reply_to(message, "Hola, bienvenido!!!")