import asyncio
from src import *
from src.bot_data import bot
from raspberry.read import get_status
from data import humidity_queries, temperature_queries

async def raspberry():
    print("Leyendo sensores...")
    i = 0
    while True:
        try:
            h, t = await get_status()
            if i == 2:
                print("guardando datos, reiniciando contador...")
                humidity_queries.insert("Un error ha ocurrido: ", h)
                temperature_queries.insert(t)
                i = 0

        except Exception as e:
            print(e)
            print("\nLecutura de sensores finalizada o sensor no conectado")
            break

        asyncio.sleep(4.5)
        i += 1

async def main():
    rasp_task = asyncio.create_task(raspberry())
    await bot.polling()

if __name__ == "__main__":
    print("Bot inicializado 🤖")
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nBot finalizado")