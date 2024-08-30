from .data import bot

@bot.message_handler(func=lambda message: True)
async def repeat(message):
    print("replying")
    await bot.reply_to(message, f"{message.text}")