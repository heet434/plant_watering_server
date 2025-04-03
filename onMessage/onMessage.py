import json
from onMessage.optimalMoisture.predict_optimal_moisture import predict_optimal_moisture
from onMessage.waterQuantity.handleWaterQuantityMsg import send_water_quantity_data
from onMessage.checkMoisture.checkMoisture import checkMoisture


def on_message(client, userData, msg):
    """
    Callback function to handle incoming messages.
    """
    print(f"Received message on topic: {msg.topic}")
    print(f"Message payload: {msg.payload.decode()}")
    payload = json.loads(msg.payload.decode())
    print(f"Decoded payload: {payload}")

    if msg.topic == "mqtt/water_quantity":
        print(f"Received water quantity message: {payload}")
        send_water_quantity_data(payload)
    elif msg.topic == "mqtt/get_optimal_moisture":
        print(f"Received conditions message: {payload}")
        optimal_moisture = predict_optimal_moisture(payload)
        print(f"Predicted optimal moisture level: {optimal_moisture}")
    elif msg.topic == "mqtt/check_moisture":
        print(f"Received moisture check message: {payload}")
        is_below_threshold = checkMoisture(payload)
        if is_below_threshold:
            print("Moisture level is below the threshold.")
        else:
            print("Moisture level is above the threshold.")