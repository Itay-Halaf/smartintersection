from fastapi import FastAPI
import paho.mqtt.client as mqtt
import sys
import time
import logging
import asyncio as ai

async def on_message(client,userdata,message):
    print("Message recieved: " + str(message.payload.decode("utf-8")))
    print('Topic: ' + str(message.topic))
    logging.log(logging.INFO, message)
    await ai.as_completed()

print('test')
client = mqtt.Client()

async def sub():
    try:
        logging.log(logging.INFO, "Starting subscriber!! ahhhh!!!")

        topic = "test/status"

        client.subscribe(topic)
        client.loop_start()

        client.on_message = await ai.coroutine(on_message) #lambda client, userdata, message:print(message)

        logging.log(logging.INFO, "Subscriber has been started successfully..")
        connection = client.connect("broker",1883,60)
        if connection != 0:
            print("Could not connect to MQTT Broker!")
            sys.exit(-1)
        while connection == 0:
            pass
    except KeyboardInterrupt:
        print("interrrupted by keyboard")
        client.disconnect() # disconnect from broker
    print("This is a print pashut")

    client.disconnect()

def main():
    sub()

app = FastAPI()

@app.get("/api/{message}")
def shtok(message: str):
    # await ai.coroutine(client.publish("test/status", message, 0))
    client.publish("test/status", message, 0)
    return {"Something": "New"}