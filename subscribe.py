from paho.mqtt import client as mqtt_client
from config import broker, port, username, password
from onMessage.onMessage import on_message
import random
import time

# def on_message(client, userdata, msg):
#         returnObject = {
#             "topic": msg.topic,
#             "payload": msg.payload.decode()
#         }
#         # print(f"Received `{returnObject['payload']}` from `{returnObject['topic']}` topic")

def subscribe(client: mqtt_client, topic: str):
    """
    Subscribe to a topic and set the callback function for incoming messages.
    """
    client.subscribe(topic)
    client.on_message = on_message