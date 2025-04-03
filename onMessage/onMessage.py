from optimalMoisture.predict_optimal_moisture import predict_optimal_moisture
from waterQuantity.handleWaterQuantityMsg import send_water_quantity_data
from checkMoisture.checkMoisture import checkMoisture


def on_message(client, userdata, msg):
    """
    Callback function to handle incoming messages.
    """
    if msg.topic == "mqtt/water_quantity":
        payload = msg.payload.decode()
        print(f"Received water quantity message: {payload}")
        send_water_quantity_data(payload)
    elif msg.topic == "mqtt/get_optimal_moisture":
        payload = msg.payload.decode()
        print(f"Received conditions message: {payload}")
        optimal_moisture = predict_optimal_moisture(payload)
        print(f"Predicted optimal moisture level: {optimal_moisture}")
    elif msg.topic == "mqtt/check_moisture":
        payload = msg.payload.decode()
        print(f"Received moisture check message: {payload}")
        is_below_threshold = checkMoisture(payload)
        if is_below_threshold:
            print("Moisture level is below the threshold.")
        else:
            print("Moisture level is above the threshold.")