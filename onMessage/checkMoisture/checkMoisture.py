from thresholdModel.getThreshold import get_threshold
def checkMoisture(payload):
    """
    Function to check if the soil moisture level is below the threshold
    """
    moisture = payload.get("soil_moisture")
    conditions = {
        "temperature": payload.get("temperature"),
        "humidity": payload.get("humidity"),
        "plantId": payload.get("plantId"),
    }
    # Get the moisture threshold
    threshold = get_threshold(conditions)
    
    # Check if the moisture level is below the threshold
    if moisture < threshold:
        return True
    else:
        return False
