import Adafruit_DHT
import time

DHT_Sensor = Adafruit_DHT.DHT22
DHT_PIN = 17

while True:
	humidity, temperature = Adafruit_DHT.read(DHT_Sensor, DHT_PIN)
	if humidity and temperature is not None:
		print("Temp={0:0.1f}C	Humidity={1:0.1f}%".format(temperature, humidity))
	else:
		print("Sensor failure. Check wiring.");
	time.sleep(5);
