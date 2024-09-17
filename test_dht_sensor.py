import asyncio
from raspberry import read_dht

async def raspi():
    while True:
        humidity, temperature = read_dht()

        if humidity is not None and temperature is not None:
            print(f'Humedad: {humidity:.1f}%\nTemperatura: {temperature:.1f}°C\n')
            asyncio.sleep(0.5)

        else:
            print("Fallo al obtener lectura!")
            break

async def main():
    raspi_task = asyncio.create_task(raspi())

if __name__ == "__main__":
    asyncio.run(main())
