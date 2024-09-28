import json
from bot.bot_data import bot
from bot.fx.handle_reports import (
    humidity_report,
    send_h_report,
    send_t_report,
    temperature_report,
)
from data.models import User
from data import humidity_queries, temperature_queries, user_queries
from datetime import datetime, time

from raspberry.load_config import load_config


async def check_conditions(h: float, t: float):
    """Cheack tempereture and humidity conditions"""

    if h > 50 and t <= 28:  # humedad alta
        users: list[User] = await user_queries.get_all()
        for user in users:
            await bot.send_message(
                user.chat_id,
                "El nivel de humedad esta demesaiado alto, pero la temperatura es agradable",
            )
        return

    elif h > 50 and t > 28:
        users: list[User] = await user_queries.get_all()
        for user in users:
            await bot.send_message(
                user.chat_id,
                f"Humedad: {h}%\nTemperatura: {t}° C\n Es posible que tengas una sensación térmica mayor a la temperatura ambiente debido al exceso de humedad",
            )
        return


async def report_state(state: bool) -> None:
    "Update reports sent status"
    config_path = "raspi_config.json"

    with open(config_path, "r") as f:
        data = json.load(f)

    data["status"]["reports_sent"] = state
    with open(config_path, "w") as f:
        json.dump(data, f, indent=4)


async def generateReports(time: datetime):
    """send reports tu users automatically"""
    data = await load_config()
    if (
        (time.hour >= 4 and time.hour <= 6) or (time.hour >= 11 and time.hour <= 14)
    ) and data["status"]["reports_sent"] == False:
        # load data
        h_data = await humidity_queries.get_from_today()
        t_data = await temperature_queries.get_from_today()

        # create reports
        h_chart, max_h, min_h = await humidity_report(h_data=h_data)
        t_chart, max_t, min_t = await temperature_report(t_data=t_data)

        # load user
        users: list[User] = await user_queries.get_all()

        # send reports
        for user in users:
            await send_h_report(user.chat_id, h_chart, max_h.value, min_h.value)
            await bot.send_message(user.chat_id, "---------------")
            await send_t_report(user.chat_id, t_chart, max_t.value, min_t.value)

        # update config status
        await report_state(True)

    else:
        await report_state(False)
