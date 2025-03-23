import pymongo

# MongoDB Connection
MONGO_URI = "mongodb://localhost:27017/"
client = pymongo.MongoClient(MONGO_URI)
db = client["travel_app"]
cab_collection = db["cabs"]

# Fetch all cabs
cabs = cab_collection.find()

# Display the data
for cab in cabs:
    print(cab)
