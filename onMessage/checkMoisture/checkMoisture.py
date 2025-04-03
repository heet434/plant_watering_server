from thresholdModel.getThreshold import getThreshold

def checkMoisture(payload):
    
    moisture = payload.get("soil_moisture")
    conditions = {
        "temperature": payload.get("temperature"),
        "humidity": payload.get("humidity"),
        "plantId": payload.get("plantId"),
    }
    # Get the moisture threshold
    threshold = getThreshold(conditions)
    
    # Check if the moisture level is below the threshold
    if moisture < threshold:
        return True
    else:
        return False
