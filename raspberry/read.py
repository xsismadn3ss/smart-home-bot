import asyncio
from raspberry.sensor_config import sensor, pin, Adafruit_DHT

async def read_dht() -> tuple:
    """get dht sensor values"""

    await asyncio.sleep(0.5)
    try:   
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        print(f"status: {humidity}%, {temperature}°C")
        return humidity, temperature
    except Exception as e:
        print(e)
        print("Lectura de sensores finalizada")


async def get_status() -> str:
    """get an string formatted of humidity and temperature"""

    humidity, temperature = await read_dht()
    return f"Humedad: {humidity:.1f}% 💧\nTemperatura: {temperature:.1f}° C 🌡️"
