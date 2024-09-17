import asyncio
from src import *
from src.bot_data import bot

async def raspberry():
    while True:
        try:
            await asyncio.sleep(1)
            print("reading...")
        except asyncio.CancelledError:
            print("\nLecutura de sensores finalizada")
            break


async def main():
    rasp_task = asyncio.create_task(raspberry())
    await bot.polling()

if __name__ == "__main__":
    print("Bot intialized 🤖")
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nBot finalizado")