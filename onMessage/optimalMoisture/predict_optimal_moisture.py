from model1.inference import inference

def predict_optimal_moisture(payload):
    """
    Function to predict the optimal moisture level based on the given conditions.
    """
   
    conditions = {
        "temperature": payload.get("temperature"),
        "humidity": payload.get("humidity"),
        "soil_moisture": payload.get("soil_moisture")
    }
    
    # Call the inference function from model1
    optimal_moisture = inference(conditions)
    
    return optimal_moisture