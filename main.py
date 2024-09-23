import asyncio
from src import *
from src.bot_data import bot
from raspberry.read import get_status

async def raspberry():
    print("Leyendo sensores...")
    while True:
        try:
            await asyncio.sleep(1)
            print(await get_status())
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