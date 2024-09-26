from .bot_data import bot
from raspberry.read import get_status
from bot.fx.check_login import login_required


@bot.message_handler(commands=["status"])
@login_required
async def status(message):
    await bot.send_message(
        chat_id=message.chat.id, 
        text= await get_status()
    )