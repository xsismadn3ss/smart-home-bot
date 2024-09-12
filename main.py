import asyncio
import datetime
from src import *
from src.bot_data import bot, temp


async def main():
    await bot.polling()

if __name__ == "__main__":
    print("Bot intialized 🤖")
    asyncio.run(main())