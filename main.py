import paho.mqtt.client as mqtt
import sys
import time


client = mqtt.Client("SmartIntersection")

connection = client.connect("localhost",1883,60)
if connection != 0:
    print("Could not connect to MQTT Broker!")
    sys.exit(-1)
else: print("Connected to broker")

def shtok(message: str):
    print(f'sending {message}')
    client.publish("test/status", message, 0)
    return {"Something": "New"}