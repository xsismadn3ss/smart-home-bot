import asyncio
from datetime import datetime
from bot import *
from bot.bot_data import bot
from raspberry import *
from raspberry.load_config import load_config

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
                await save_data(h_list, t_list)
                i = 0

            await check_conditions(h,t)
            current_time = datetime.now()
            print(current_time)
            await generateReports(current_time)
            

        except Exception as e:
            print(e)
            break
        i += 1

async def bot_procces():
    await bot.polling()



async def main():
    print("Iniciando procesos...")
    raspberry_task = asyncio.create_task(raspberry())
    bot_task = asyncio.create_task(bot_procces())
    asyncio.gather(raspberry_task, bot_task)

if __name__ == "__main__":
    print("Bot inicializado 🤖")
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nBot finalizado")