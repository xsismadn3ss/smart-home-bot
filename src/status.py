from .bot_data import bot
from raspberry.read import read_dht, get_status

@bot.message_handler(commands=["status"])
async def status(message):
    # humidity, temperature = await read_dht()
    await bot.send_message(
        chat_id=message.chat.id, 
        # text=f"Humedad:{humidity:.1f}%\nTemperature: {temperature:.1f}"
        text= await get_status()
    )