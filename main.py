import asyncio
from src import *
from src.bot_data import bot
from raspberry.read import read_dht
from data import humidity_queries, temperature_queries

async def raspberry():
    print("Leyendo sensores...")
    while True:
        try:
            data = await get_status()
            h = data[0]
            t = data[1]
            print(f"guardando datos: {h}%, {t}°C")
            # await humidity_queries.insert(data[0])
            # await temperature_queries.insert(data[1])
            await asyncio.sleep(2.5) 

        except Exception as e:
            print(e)
            print("\nLecutura de sensores finalizada o sensor no conectado")
            break


async def main():
    rasp_task = asyncio.create_task(raspberry())
    await bot.polling()

if __name__ == "__main__":
    print("Bot inicializado 🤖")
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nBot finalizado")