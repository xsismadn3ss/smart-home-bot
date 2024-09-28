import asyncio
from datetime import datetime
from bot.bot_data import bot
from bot import *
from raspberry.read import read_dht
from raspberry.handle_data import save_data
from raspberry.events import check_conditions, generateReports


async def raspberry():
    print("Leyendo sensores...")
    i = 0
    h_list = []
    t_list = []
    while True:
        time = datetime.now()
        print("Hora actual: {}:{}:{}".format(time.hour, time.minute, time.second))
        try:
            h, t = await read_dht()
            t_list.append(t)
            h_list.append(h)
            if i == 20:
                h_list, t_list, i = await save_data(h_list, t_list, i)
            generateReports(time)

        except Exception as e:
            print(e)
            break
        i += 1


async def reports():
    current_time = datetime.now()
    print(current_time.hour)
    await generateReports(current_time)
    await asyncio.sleep(5)
    reports()


async def main():
    print("Iniciando procesos...")

    raspberry_task = asyncio.create_task(raspberry())
    # reports_task = asyncio.create_task(reports())
    await bot.polling()

    # asyncio.gather(raspberry_task, reports_task)


if __name__ == "__main__":
    print("Bot inicializado 🤖")
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nBot finalizado")
