import requests
import pymongo

url = "https://irctc1.p.rapidapi.com/api/v3/trainBetweenStations"

querystring = {"fromStationCode":"BVI","toStationCode":"NDLS","dateOfJourney":"2025-03-27"}

headers = {
	'x-rapidapi-key': "1fed74745amshe1f9cbb68d5bbb5p1c68f6jsn185d2958cdc0",
	'x-rapidapi-host': "irctc1.p.rapidapi.com"
}


# Fetch API Data
try:
    response = requests.get(url, headers=headers, params=querystring)
    response.raise_for_status()  # Check for errors
    train_data = response.json().get("data", [])  # Extract train list
except requests.exceptions.RequestException as e:
    print(f"Error fetching data: {e}")
    train_data = []

# Connect to MongoDB
MONGO_URI = "mongodb://localhost:27017"  # Change this to MongoDB Atlas URI if needed
client = pymongo.MongoClient(MONGO_URI)
db = client["TrainDatabase"]  # Database Name
collection = db["Trains"]  # Collection Name

# Insert Data into MongoDB
if train_data:
    for train in train_data:
        train_doc = {
            "_id": train.get("train_number"),  # Use train number as unique ID
            "train_name": train.get("train_name"),
            "source": train.get("from_station"),
            "destination": train.get("to_station"),
            "departure_time": train.get("departure_time"),
            "arrival_time": train.get("arrival_time"),
            "duration": train.get("duration")
        }
        collection.update_one({"_id": train_doc["_id"]}, {"$set": train_doc}, upsert=True)

    print("Data inserted into MongoDB successfully!")
else:
    print("No train data available.")

# Retrieve & Display Data (Optional)
for train in collection.find():
    print(train)