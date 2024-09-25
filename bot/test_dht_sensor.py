import asyncio
from raspberry import read_dht


# async def read_sensor():
#     await asyncio.sleep(0.3)
#     humidity, temperature = read_dht()
#     return humidity, temperature


async def main():
    while True:
        humidity, temperature = await read_dht()

        if humidity is not None and temperature is not None:
            print(f"Humedad: {humidity:.1f}%\nTemperatura: {temperature:.1f}°C\n")
        else:
            print("Fallo al obtener lectura!")


if __name__ == "__main__":
    asyncio.run(main())
