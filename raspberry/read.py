from sensor_config import sensor, pin, Adafruit_DHT

def read_dht() -> tuple:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    return humidity, temperature