import asyncio
from commands import *
from commands.data import bot, temp
from commands.queries.users_queries import get_users
import datetime

async def count():
    i = 1
    ids = await get_users()
    while True:
        print(datetime.datetime.now())
        i += 1
        await asyncio.sleep(1)
        if i == 10:
            print("event trigger")
            for id in ids:
                chat_id=id[1]
                print("Sending message to ", chat_id)
                await bot.send_message(chat_id, "Un evento ha ocurrido!!!")
                

async def main():
    count_task = asyncio.create_task(count())
    asyncio.gather(count_task)

    print("bot initialized 🤖")
    await bot.polling()

if __name__ == "__main__":
    asyncio.run(main())