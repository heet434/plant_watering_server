# Send water quantity data to the mongodb database

from pymongo import MongoClient
from config import mongo_uri, mongo_db, mongo_collection

def send_water_quantity_data(payload):
    """
    Function to send water quantity data to the MongoDB database.
    """
    # Assuming you have a MongoDB client and database set up
    # Connect to MongoDB
    client = MongoClient(mongo_uri)
    db = client[mongo_db]
    collection = db[mongo_collection]

    # Prepare the data to be inserted
    data = {
        "water_quantity": payload.get("water_quantity"),
        "session_id": payload.get("session_id")
    }

    # Find the document with the same session_id
    existing_document = collection.find_one({"session_id": data["session_id"]})
    if existing_document:
        # Update the existing document with the new water quantity
        collection.update_one(
            {"session_id": data["session_id"]},
            {"$set": {"water_quantity": data["water_quantity"]}}
        )
        print(f"Updated document with session_id {data['session_id']}")
    
    else:
        print(f"Session ID {data['session_id']} not found in the database.")
        
    client.close()
    
