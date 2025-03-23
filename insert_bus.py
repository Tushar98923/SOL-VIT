import pymongo

# MongoDB Connection
MONGO_URI = "mongodb://localhost:27017/"
client = pymongo.MongoClient(MONGO_URI)
db = client["travel_app"]
bus_collection = db["buses"]

# Bus Data
buses = [
    {"bus_no": "MH101", "start": "Mumbai", "end": "Pune", "stops": ["Lonavala"], "departure": "06:00", "arrival": "09:30", "type": "AC Sleeper"},
    {"bus_no": "DL202", "start": "Delhi", "end": "Jaipur", "stops": ["Gurgaon", "Rewari"], "departure": "07:30", "arrival": "12:00", "type": "Volvo"},
    {"bus_no": "KA303", "start": "Bangalore", "end": "Mysore", "stops": ["Ramanagara"], "departure": "08:00", "arrival": "10:30", "type": "Non-AC"},
    {"bus_no": "TN404", "start": "Chennai", "end": "Coimbatore", "stops": ["Vellore", "Salem"], "departure": "09:00", "arrival": "15:00", "type": "AC"},
    {"bus_no": "WB505", "start": "Kolkata", "end": "Durgapur", "stops": ["Bardhaman"], "departure": "10:00", "arrival": "13:00", "type": "Semi-Sleeper"},
    {"bus_no": "RJ606", "start": "Jaipur", "end": "Udaipur", "stops": ["Ajmer"], "departure": "11:00", "arrival": "17:00", "type": "Luxury"},
    {"bus_no": "MP707", "start": "Bhopal", "end": "Indore", "stops": ["Sehore", "Dewas"], "departure": "12:00", "arrival": "15:00", "type": "Deluxe"},
    {"bus_no": "TS808", "start": "Hyderabad", "end": "Vijayawada", "stops": ["Suryapet"], "departure": "13:00", "arrival": "17:00", "type": "AC Sleeper"},
    {"bus_no": "GJ909", "start": "Ahmedabad", "end": "Surat", "stops": ["Vadodara"], "departure": "14:00", "arrival": "18:00", "type": "Luxury"},
    {"bus_no": "PB1010", "start": "Chandigarh", "end": "Amritsar", "stops": ["Ludhiana", "Jalandhar"], "departure": "15:00", "arrival": "20:00", "type": "Volvo"},
]

# Insert into MongoDB
bus_collection.insert_many(buses)

print("Bus data inserted successfully!")
