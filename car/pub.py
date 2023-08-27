import paho.mqtt.client as mqtt
import sys
import time

client = mqtt.Client()

connection = client.connect("localhost",1883,60)
if connection != 0:
    print("Could not connect to MQTT Broker!")
    sys.exit(-1)
client.publish("test/status","This is a test!",0)


client.disconnect()
