from .bot_data import bot
from raspberry.read import get_status

@bot.message_handler(commands=["status"])
async def status(message):
    await bot.send_message(
        chat_id=message.chat.id, 
        text= await get_status()
    )