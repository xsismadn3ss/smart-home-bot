from data import humidity_queries, temperature_queries
from data.models import Humidity, Temperature
from bot.fx.handle_charts import h_chart, t_chart, send_chart
from bot.bot_data import bot


async def send_h_report(chat_id:int, h_chart:str, max_h:float, min_h:float) -> None:
    """Send Humidity Report"""
    await bot.send_message(chat_id, "Gráfica de Humedad")
    await send_chart(h_chart, chat_id)
    await bot.send_message(chat_id, f"Máxima: {max_h}% | Mínima: {min_h}%")


async def send_t_report(chat_id, t_chart, max_t, min_t) -> None:
    """Send Temperature Report"""
    await bot.send_message(chat_id, "Gráfica de Temperatua")
    await send_chart(t_chart, chat_id)
    await bot.send_message(chat_id, f"Máxima: {max_t}° C | Mínima: {min_t}° C")


async def humidity_report(h_data: list[Humidity]) -> tuple[str, float, float]:
    """Generate humidity report

    Output:
    ```
    humidity_chart: str
    max_h: float
    min_h: float

    return humidity_chart, max_h, min_h
    ```
    """
    humidity_chart = await h_chart(h_data)
    max_h = await humidity_queries.get_max(h_data)
    min_h = await humidity_queries.get_min(h_data)
    return humidity_chart, max_h, min_h


async def temperature_report(t_data: list[Temperature]) -> tuple[str, float, float]:
    """Generate temperature report

    Output:
     ```
    temperature_chart: str
    max_t: float
    min_t: float

    return temperature_chart, max_t, min_t
    ```
    """
    temperature_chart = await t_chart(t_data)
    max_t = await temperature_queries.get_max(t_data)
    min_t = await temperature_queries.get_min(t_data)
    return temperature_chart, max_t, min_t
