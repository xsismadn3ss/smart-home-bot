from .bot_data import bot

@bot.message_handler(commands=["status"])
async def status(message):
    print("enviando status")
    state = "La temperatura actual es:...\nLa humedad actual es:..."
    await bot.send_message(chat_id=message.chat_id, text=state)