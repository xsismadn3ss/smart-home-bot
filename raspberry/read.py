from .sensor_config import sensor, pin, Adafruit_DHT

async def read_dht() -> tuple:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    print("enviando datos")
    print(humidity, temperature)
    return humidity, temperature

def get_status() -> str:
    humidity, temperature = read_dht()
    return f"Humedad:{humidity:.1f}%\nTemperature: {temperature:.1f}"