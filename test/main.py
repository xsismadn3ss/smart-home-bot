import asyncio
from commands import *
from commands.data import bot

async def count():
    i = 1
    while True:
        print(f"Lectura {i}")
        i+=1
        await asyncio.sleep(1)

async def main():
    count_task = asyncio.create_task(count())
    asyncio.gather(count_task)

    print("bot initialized 🤖")
    await bot.polling()

if __name__ == "__main__":
    asyncio.run(main())