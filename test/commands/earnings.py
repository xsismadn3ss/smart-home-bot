from .data import bot
from .data import temp
from .queries.earn_queries import get_all, insert

@bot.message_handler(commands=["save_earn"])
async def save_earning(message):
    print("ask info")
    chat_id = message.chat.id
    temp[chat_id] = 'saving earning'
    await bot.reply_to(message, "Ingresa tu ganancia en el siguiente formato...")
    await bot.send_message(chat_id, "'cantidad' | ' razon'")


@bot.message_handler(func=lambda message: temp.get(message.chat.id)== 'saving earning')
async def process_data(message):
    try:
        print("saving info...")
        success = await insert((message.text))
        if success:
            await bot.send_message(message.chat.id, "Datos guardados con exito 🎉")
        else:
            await bot.send_message(message.chat.id, "Error guardando los datos")
        temp[message.chat.id] = None
    except Exception as e:
        await bot.reply_to(message, f"Ha sucedido un error {e}")


@bot.message_handler(commands=["get_earnings"])
async def load_earnings(message):
    try:
        print("loading info...")
        msg = ""
        data = await get_all()
        for d in data:
            msg += f"- {d[2]} | {d[3]}\n"
        await bot.reply_to(message, "Ganancias: ")
        await bot.send_message(message.chat.id, msg)
    except Exception as e:
        print(e)
        await bot.send_message(message.chat.id, "Aún no hay información guardada")