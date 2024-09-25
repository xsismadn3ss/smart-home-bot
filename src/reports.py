from src.fx.check_login import login_required
from .bot_data import bot
from src.fx import handle_charts


@bot.message_handler(commands=["reports"])
@login_required
async def reports(message):
    h = handle_charts.h_chart(message)

    if h is not None:
        handle_charts.send_chart(h, message)

    else:
        await bot.send_message(
            message.chat.id, "No se pudo crear la grafica, intenta de nuevo"
        )
