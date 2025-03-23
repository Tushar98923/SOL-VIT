import pymongo

# MongoDB Connection
MONGO_URI = "mongodb://localhost:27017/"
client = pymongo.MongoClient(MONGO_URI)
db = client["travel_app"]
bus_collection = db["buses"]

# Fetch and Display All Bus Data
buses = bus_collection.find()

print("List of Buses:")
for bus in buses:
    print(bus)
