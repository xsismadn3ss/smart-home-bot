import asyncio
from src import *
from src.bot_data import bot
from raspberry.read import read_dht

async def raspberry():
    print("Leyendo sensores...")
    while True:
        try:
            data = await read_dht()
            print(data)
        except asyncio.CancelledError:
            print("\nLecutura de sensores finalizada")
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