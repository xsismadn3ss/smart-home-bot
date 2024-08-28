from .data import bot

# reapeat message
@bot.message_handler(func=lambda message: True)
def repeat(message):
    print("replying")
    bot.reply_to(message, f"{message.text}")