import asyncio
from src import *
from src.bot_data import bot
from raspberry.read import read_dht
from data import humidity_queries, temperature_queries

async def raspberry():
    print("Leyendo sensores...")
    while True:
        try:
            h, t = await read_dht()
            print(f"status: {h}%, {t}°C")
            await humidity_queries.insert(h)
            await temperature_queries.insert(t)
            await asyncio.sleep(2.5) 

        except Exception as e:
            print(e)
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