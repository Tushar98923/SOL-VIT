import pymongo

# MongoDB Connection
MONGO_URI = "mongodb://localhost:27017/"
client = pymongo.MongoClient(MONGO_URI)
db = client["travel_app"]
bus_collection = db["buses"]

# Next 10 Unique Bus Records
buses = [
    {"bus_no": "RJ445", "start": "Jaipur", "end": "Mount Abu", "stops": ["Ajmer", "Pali"], "departure": "19:00", "arrival": "05:00", "type": "Sleeper AC"},
    {"bus_no": "KA556", "start": "Bangalore", "end": "Coorg", "stops": ["Mysore"], "departure": "07:00", "arrival": "12:00", "type": "Luxury"},
    {"bus_no": "DL667", "start": "Delhi", "end": "Nainital", "stops": ["Gurgaon", "Moradabad"], "departure": "21:30", "arrival": "07:00", "type": "Semi-Sleeper"},
    {"bus_no": "WB778", "start": "Kolkata", "end": "Digha", "stops": ["Kharagpur"], "departure": "06:00", "arrival": "11:00", "type": "AC Seater"},
    {"bus_no": "GJ889", "start": "Ahmedabad", "end": "Dwarka", "stops": ["Rajkot", "Jamnagar"], "departure": "20:00", "arrival": "08:00", "type": "Sleeper"},
    {"bus_no": "TN990", "start": "Madurai", "end": "Kodaikanal", "stops": ["Dindigul"], "departure": "08:30", "arrival": "13:00", "type": "Mini Bus"},
    {"bus_no": "MH101", "start": "Pune", "end": "Shirdi", "stops": ["Nashik"], "departure": "05:30", "arrival": "11:00", "type": "AC Seater"},
    {"bus_no": "HR202", "start": "Chandigarh", "end": "Shimla", "stops": ["Solan"], "departure": "10:00", "arrival": "15:00", "type": "Luxury Coach"},
    {"bus_no": "BR303", "start": "Patna", "end": "Bodh Gaya", "stops": ["Gaya"], "departure": "14:00", "arrival": "17:30", "type": "Deluxe"},
    {"bus_no": "UP404", "start": "Lucknow", "end": "Varanasi", "stops": ["Prayagraj"], "departure": "18:00", "arrival": "00:30", "type": "Volvo Sleeper"},
]

# Insert data into MongoDB
bus_collection.insert_many(buses)

print("Next 10 unique bus records inserted successfully.")
