import paho.mqtt.client as mqtt 
import json
from firebase_handler import FirebaseHandler
from time import sleep

firebase = FirebaseHandler()

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker")
    else:
        print("Failed to connect, return code %d\n", rc)


def on_message(client, userdata, msg):
    payload = msg.payload.decode()
    jsonObj = json.loads(payload)
    print(jsonObj)
    firebase.save(jsonObj['temperature'], jsonObj['humidity'])
    sleep(5)


def main():
    topic = "climate/+"
    client = mqtt.Client()
    client.on_connect = on_connect
    client.connect('localhost')
    client.subscribe(topic)
    client.on_message = on_message

    client.loop_forever()


if __name__ == '__main__':
    main()