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
                "Humedad: {h}%\nTemperatura: {t}° C\n Es posible que tengas una sensación térmica mayor a la temperatura ambiente debido al exceso de humedad",
            )
        return


async def report_state(state: bool) -> None:
    "Update reports sent status"
    config_path = "raspi_config.json"

    with open(config_path, "r") as f:
        data = json.load(f)

    data["status"]["reports_sent"] = state
    with open(config_path, "w") as f:
        json.dump(data, config_path, indent=4)


async def generateReports(time: datetime):

    if time.hour > 20 and load_config()["status"]["reports_sents"] == False:
        # load data
        h_data = await humidity_queries.get_from_today()
        t_data = await temperature_queries.get_from_today()

        # create reports
        h_chart, max_h, min_h = await humidity_report(h_data=h_data)
        t_chart, max_t, min_t = await temperature_report(h_data=h_data)

        # load user
        users: list[User] = await user_queries.get_all()

        # send reports
        for user in users:
            await send_h_report(user.chat_id, h_chart, max_h, min_h)
            await bot.send_message(user.chat_id, "---------------")
            await send_t_report(user.chat_id, t_chart, max_t, min_t)

        # update config status
        report_state(True)

    report_state(False)
