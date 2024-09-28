import asyncio
from raspberry.read import read_dht

async def main():
    while True:
        humidity, temperature = await read_dht()

        if humidity is not None and temperature is not None:
            print("El sensor funciona correctamente")
        else:
            print("Fallo al obtener lectura!")


if __name__ == "__main__":
    asyncio.run(main())
