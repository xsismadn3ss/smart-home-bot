from src.fx.check_login import login_required
from .bot_data import bot
from src.fx import handle_charts


@bot.message_handler(commands=["reports"])
@login_required
async def reports(message):
    h = await handle_charts.h_chart()
    t = await handle_charts.t_chart()
    chatid = message.chat.id

    if h is not None:
        await bot.send_message(chatid, "Grafica de humedad")
        await handle_charts.send_chart(h, message)
    if t is not None:
        await bot.send_message(chatid, "Grafica de temperatura")
        await handle_charts.send_chart(t, message)

    else:
        await bot.send_message(
            message.chat.id, "No se pudo crear la grafica, intenta de nuevo"
        )
