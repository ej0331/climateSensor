import Adafruit_DHT
import time
import paho.mqtt.client as mqtt
import json 


dht11 = Adafruit_DHT.DHT11
DHT_PIN = 4


client = mqtt.Client()
client.connect('localhost')
while True:
    h, t = Adafruit_DHT.read_retry(dht11, DHT_PIN)
    print(h, t)
    client.publish(f"climate/data", json.dumps({"temperature": t, "humidity": h}))
    time.sleep(1)