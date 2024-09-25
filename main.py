import asyncio
from src import *
from src.bot_data import bot
from raspberry.read import get_status
from data import humidity_queries, temperature_queries

async def raspberry():
    print("Leyendo sensores...")
    while True:
        try:
            h, t = await get_status()
            print(h,t)
            print("guardando datos: {}%, {}°C".format(h, t))
            humidity_queries.insert(h)
            temperature_queries.insert(t)
            asyncio.sleep(4.5) 

        except Exception as e:
            print("Un error ha ocurrido: ",e)
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