import asyncio
import datetime
from src import *
from src.bot_data import bot

async def raspberry():
    while True:
        await asyncio.sleep(2)


async def main():
    rasp_task = asyncio.create_task(raspberry())
    asyncio.gather(rasp_task)
    await bot.polling()

if __name__ == "__main__":
    print("Bot intialized 🤖")
    asyncio.run(main())