import asyncio
from bot import *
from bot.bot_data import bot
from raspberry import *

async def raspberry():
    print("Leyendo sensores...")
    i = 0
    h_list = []
    t_list = []
    while True:
        try:
            h, t = await read_dht()
            print(f"status: {h}%, {t}°C")
            t_list.append(t)
            h_list.append(h)

            if i == 5:
                print("creando promedio y guardando")
                save_data(h_list, t_list)

        except Exception as e:
            print(e)
            break

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