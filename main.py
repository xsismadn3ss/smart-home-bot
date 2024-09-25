import asyncio
from src import *
from src.bot_data import bot
from raspberry.read import read_dht
from data import humidity_queries, temperature_queries

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

            if i == 30:
                print("creando promedio y guardando")
                print(t_list)
                t_avg = sum(t_list) / len(t_list)
                t_list = []
                i = 0

                await humidity_queries.insert(t_avg)
                # await temperature_queries.insert(t)


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