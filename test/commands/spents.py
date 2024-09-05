from .data import bot
from .data import temp
from .queries.spent_queries import get_all, insert

@bot.message_handler(commands=['save_spent'])
async def save_spent(message):
    print("ask info")
    chatid = message.chat.id
    temp[chatid] = 'saving spent'
    await bot.reply_to(message, "Ingresa el gasto en el siguiente formato")
    await bot.send_message(chatid, "'cantidad' | 'razon'")

@bot.message_handler(func=lambda message: temp.get(message.chat.id)== 'saving spent')
async def procces_data(message):
    try:
        print("saving info")
        succes = await insert(message.text)
        if succes:
            await bot.send_message(message.chat.id, "Datos guardados con exito 🎉")
        else:
            await bot.send_message(message.chat.id, "Hubo un error ☹️")
        temp[message.chat.id]=None
    except Exception as e:
        await bot.reply_to(message, f"ha sucedido un error {e}")

@bot.message_handler(commands=["get_expense"])
async def load_expense(message):
    print(type(message))
    try:
        print("loading info...")
        msg = []
        data = await get_all()
        for d in data:
            msg.append(f"- {d[2]} | {d[3]}\n")
        await bot.reply_to(message, 'Gastos')
        await bot.send_message(message.chat.id, "".join(msg))
    except Exception as e:
        print(e)
        await bot.send_message(message.chat.id, "Aún no hay información guardada")