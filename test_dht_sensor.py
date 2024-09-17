import time
from raspberry import read_dht
# import Adafruit_DHT

# sensor = Adafruit_DHT.DHT11
# pin = 4

while True:
    # humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    humidity, temperature = read_dht()

    if humidity is not None and temperature is not None:
        print(f'Humedad: {humidity:.1f}%\nTemperatura: {temperature:.1f}°C\n')

    else:
        print("Fallo al obtener lectura!")

    time.sleep(0.5)