import asyncio
from datetime import datetime
from bot.bot_data import bot
from raspberry.read import read_dht
from raspberry.handle_data import save_data
from raspberry.events import check_conditions, generateReports

async def raspberry():
    print("Leyendo sensores...")
    i = 0
    h_list = []
    t_list = []
    while True:
        try:
            h, t = await read_dht()
            t_list.append(t); h_list.append(h)
            if i == 5:
                h_list, t_list, i = await save_data(h_list, t_list)

            # await check_conditions(h,t)            

        except Exception as e:
            print(e)
            break
        i += 1

async def reports():
    current_time = datetime.now()
    print(current_time)
    await generateReports(current_time)


async def main():
    print("Iniciando procesos...")
    raspberry_task = asyncio.create_task(raspberry())
    reports_task = asyncio.create_task(reports())
    asyncio.gather(raspberry_task, reports_task)
    await bot.polling()

if __name__ == "__main__":
    print("Bot inicializado 🤖")
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nBot finalizado")