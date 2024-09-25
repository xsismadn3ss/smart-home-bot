from src.fx import check_login
from .bot_data import bot
from src.fx import handle_charts


@bot.message_handler(commands=["reports"])
@check_login
async def reports(message):
    h = handle_charts.h_chart()

    if h is not None:
        handle_charts.send_chart(h)

    else:
        await bot.send_message(
            message.chat.id, "No se pudo crear la grafica, intenta de nuevo"
        )
