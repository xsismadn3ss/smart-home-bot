from .sensor_config import sensor, pin, Adafruit_DHT

async def read_dht() -> tuple:
    data = await Adafruit_DHT.read_retry(sensor, pin)
    print(data)
    return data

async def get_status() -> str:
    data = await read_dht()
    return f"Humedad:{data[0]:.1f}%\nTemperature: {data[1]:.1f}"