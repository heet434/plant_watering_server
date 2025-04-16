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
    # print(f"Received message on topic: {msg.topic}")
    # print(f"Message payload: {msg.payload.decode()}")
    payload = json.loads(msg.payload.decode())
    # print(f"Decoded payload: {payload}")

    if msg.topic == "mqtt/moisture_alert":
        print("=====================")
        print(f"Received moisture alert message: {payload}")
        print("---------------------")
        print(f'Stopping water supply for plant: {payload["plant_id"]}')
        print(f"Current soil moisture: {payload['soil_moisture_now']}")
        print(f"Water quantity used: {payload['water_quantity']}")
        sent_data = send_water_quantity_data(payload)
        print("Saved water quantity data in db")
        print("=====================")
    elif msg.topic == "mqtt/get_optimal_moisture":
        print("=====================")
        print(f"Current moisture level: {payload['soil_moisture_now']}")
        optimal_moisture = predict_optimal_moisture(payload)
        print(f"Predicted optimal moisture level: {optimal_moisture}")
        optimal_moisture = str(optimal_moisture)
        if optimal_moisture > payload['soil_moisture_now']:
            print(f"Watering plant: {payload['plant_id']}")
        else:
            print("Plant conditions fine.")
        publish(client, "mqtt/optimal_moisture_threshold", optimal_moisture)
        print("=====================")
    elif msg.topic == "mqtt/get_water_quantity":
        print("=====================")
        print(f"Current conditions: {payload}")
        water_quantity = predict_water_quantity(payload)
        print(f"Add {water_quantity} liters of water to the plant: {payload['plant_id']}")
        water_quantity = str(water_quantity)
        publish(client, "mqtt/water_quantity", water_quantity)
        print("=====================")
    else:
        print("=====================")
        print(f"Unknown topic: {msg.topic}")
        print("No action taken.")
        print("=====================")
        return
    # print("=========================================")
    # print("Message processed successfully.")
    # print("=========================================")
    