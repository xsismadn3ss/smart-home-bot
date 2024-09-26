from bot.fx.check_login import login_required
from .bot_data import bot

@bot.message_handler(commands=["start"])
@login_required
async def welcome(message):
    print("Greeting")
    await bot.reply_to(message,"Bienvenido")