import asyncio
from src import *
from src.bot_data import bot

async def raspberry():
    while True:
        try:
            await asyncio.sleep(1)
            print("reading...")
        except asyncio.CancelledError:
            print("Lecutura de sensores finalizada")
            break


async def main():
    try:
        rasp_task = asyncio.create_task(raspberry())
        await bot.polling()
        # asyncio.gather(rasp_task)
    except KeyboardInterrupt:
        print("Bot finalizado")
    finally:
        rasp_task.cancel()
        await rasp_task

if __name__ == "__main__":
    print("Bot intialized 🤖")
    asyncio.run(main())