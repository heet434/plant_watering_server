from paho.mqtt import client as mqtt_client
from config import broker, port, username, password
import random
import time

def on_message(client, userdata, msg):
        returnObject = {
            "topic": msg.topic,
            "payload": msg.payload.decode()
        }
        print(f"Received `{returnObject['payload']}` from `{returnObject['topic']}` topic")

def subscribe(client: mqtt_client, topic: str, on_message_callback = on_message):
    """
    Subscribe to a topic and set the callback function for incoming messages.
    """
    client.subscribe(topic)
    client.on_message = on_message