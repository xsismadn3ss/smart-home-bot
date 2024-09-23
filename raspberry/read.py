import asyncio
from .sensor_config import sensor, pin, Adafruit_DHT

async def read_dht() -> tuple:
    await asyncio.sleep(0.5)
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    return humidity, temperature

async def get_status() -> str:
    humidity, temperature = await read_dht()
    return f"Humedad: {humidity:.1f}% 💧\nTemperature: {temperature:.1f} 🌡️"