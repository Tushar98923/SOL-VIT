import pymongo

# MongoDB Connection
MONGO_URI = "mongodb://localhost:27017/"
client = pymongo.MongoClient(MONGO_URI)
db = client["travel_app"]
bus_collection = db["buses"]

# Next 10 Unique Bus Records
buses = [
    {"bus_no": "HR112", "start": "Delhi", "end": "Manali", "stops": ["Ambala", "Mandi", "Kullu"], "departure": "19:00", "arrival": "07:00", "type": "Volvo Sleeper"},
    {"bus_no": "PB223", "start": "Amritsar", "end": "Chandigarh", "stops": ["Jalandhar", "Ludhiana"], "departure": "08:30", "arrival": "12:30", "type": "Express"},
    {"bus_no": "GJ334", "start": "Surat", "end": "Mumbai", "stops": ["Valsad", "Vapi"], "departure": "06:45", "arrival": "11:15", "type": "AC Seater"},
    {"bus_no": "MH445", "start": "Pune", "end": "Nashik", "stops": ["Ahmednagar", "Shirdi"], "departure": "10:00", "arrival": "15:00", "type": "Luxury"},
    {"bus_no": "RJ556", "start": "Udaipur", "end": "Jodhpur", "stops": ["Pali", "Falna"], "departure": "07:00", "arrival": "12:30", "type": "Express"},
    {"bus_no": "KA667", "start": "Mangalore", "end": "Bangalore", "stops": ["Udupi", "Hassan"], "departure": "21:30", "arrival": "06:00", "type": "Volvo Sleeper"},
    {"bus_no": "KL778", "start": "Trivandrum", "end": "Kochi", "stops": ["Kollam", "Alleppey"], "departure": "08:00", "arrival": "12:00", "type": "AC Seater"},
    {"bus_no": "MP889", "start": "Indore", "end": "Gwalior", "stops": ["Bhopal", "Shivpuri"], "departure": "09:00", "arrival": "18:00", "type": "Luxury"},
    {"bus_no": "UP990", "start": "Varanasi", "end": "Allahabad", "stops": ["Mirzapur"], "departure": "11:00", "arrival": "14:00", "type": "Express"},
    {"bus_no": "CG101", "start": "Bilaspur", "end": "Raigarh", "stops": ["Champa", "Korba"], "departure": "07:30", "arrival": "11:30", "type": "Luxury"}
]

# Insert into MongoDB
bus_collection.insert_many(buses)

print("Next 10 buses inserted successfully!")
