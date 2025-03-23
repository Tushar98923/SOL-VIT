from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")  # Update URI if needed
db = client["travel_app"]  # Switch to the correct database

# List of collections to update
collections_to_update = ["cabs", "trains", "buses", "flights"]

# Define the update pipeline to rename fields and remove old ones
pipeline = [
    {
        "$set": {
            "source": "$start",
            "destination": "$end"
        }
    },
    {
        "$unset": ["start", "end"]
    }
]

# Iterate over all collections and apply the updates
for collection_name in collections_to_update:
    collection = db[collection_name]
    
    # Find records where 'start' and 'end' exist
    query = {"start": {"$exists": True}}
    
    # Update matching records
    result = collection.update_many(query, pipeline)
    
    # Print the result for each collection
    print(f"Collection: {collection_name}")
    print(f"Matched records: {result.matched_count}")
    print(f"Modified records: {result.modified_count}")
    print("-" * 40)

# Verify updates (Optional: Print updated records)
for collection_name in collections_to_update:
    collection = db[collection_name]
    updated_records = collection.find({"source": {"$exists": True}})
    
    print(f"Updated records in '{collection_name}':")
    for record in updated_records:
        print(record)
    print("-" * 40)
