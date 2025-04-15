import json
from paho.mqtt import client as mqtt_client

from onMessage.optimalMoisture.predict_optimal_moisture import predict_optimal_moisture
from onMessage.waterQuantity.handleWaterQuantityMsg import send_water_quantity_data
from onMessage.predictWaterQuantity.predict_water_quantity import predict_water_quantity

from publish import publish


def on_message(client: mqtt_client, userData, msg: str):
    """
    Callback function to handle incoming messages.
    """
    print(f"Received message on topic: {msg.topic}")
    print(f"Message payload: {msg.payload.decode()}")
    payload = json.loads(msg.payload.decode())
    print(f"Decoded payload: {payload}")

    if msg.topic == "mqtt/moisture_alert":
        print(f"Received moisture alert message: {payload}")
        sent_data = send_water_quantity_data(payload)
        print(f"Sent data to MongoDB: {sent_data}")
    elif msg.topic == "mqtt/get_optimal_moisture":
        print(f"Received conditions message: {payload}")
        optimal_moisture = predict_optimal_moisture(payload)
        print(f"Predicted optimal moisture level: {optimal_moisture}")
        optimal_moisture = str(optimal_moisture)
        publish(client, "mqtt/optimal_moisture_threshold", optimal_moisture)
    elif msg.topic == "mqtt/get_water_quantity":
        print(f"Received water quantity message: {payload}")
        water_quantity = predict_water_quantity(payload)
        print(f"Predicted water quantity: {water_quantity}")
        water_quantity = str(water_quantity)
        publish(client, "mqtt/water_quantity", water_quantity)
    else:
        print(f"Unknown topic: {msg.topic}")
        print("No action taken.")
        return
    print("Message processed successfully.")
    print("=========================================")
    