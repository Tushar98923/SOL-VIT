import pymongo

# MongoDB Connection
MONGO_URI = "mongodb://localhost:27017/"
client = pymongo.MongoClient(MONGO_URI)
db = client["travel_app"]
bus_collection = db["buses"]

# Next 10 Unique Bus Records
buses = [
    {"bus_no": "TN505", "start": "Chennai", "end": "Pondicherry", "stops": ["Mahabalipuram"], "departure": "07:00", "arrival": "10:30", "type": "Luxury AC"},
    {"bus_no": "MH606", "start": "Mumbai", "end": "Mahabaleshwar", "stops": ["Pune", "Wai"], "departure": "22:00", "arrival": "06:00", "type": "Sleeper AC"},
    {"bus_no": "RJ707", "start": "Jodhpur", "end": "Udaipur", "stops": ["Pali", "Ranakpur"], "departure": "08:00", "arrival": "14:00", "type": "Deluxe"},
    {"bus_no": "KL808", "start": "Kochi", "end": "Munnar", "stops": ["Ernakulam"], "departure": "06:30", "arrival": "11:00", "type": "AC Seater"},
    {"bus_no": "MP909", "start": "Bhopal", "end": "Indore", "stops": ["Ujjain"], "departure": "17:30", "arrival": "21:00", "type": "Volvo AC"},
    {"bus_no": "AS101", "start": "Guwahati", "end": "Shillong", "stops": ["Nongpoh"], "departure": "09:00", "arrival": "13:00", "type": "Luxury AC"},
    {"bus_no": "PB202", "start": "Amritsar", "end": "Dharamshala", "stops": ["Pathankot"], "departure": "19:30", "arrival": "05:30", "type": "Sleeper"},
    {"bus_no": "OD303", "start": "Bhubaneswar", "end": "Puri", "stops": ["Khordha"], "departure": "12:00", "arrival": "14:30", "type": "Deluxe"},
    {"bus_no": "CG404", "start": "Raipur", "end": "Jagdalpur", "stops": ["Kanker"], "departure": "18:00", "arrival": "06:00", "type": "Sleeper AC"},
    {"bus_no": "HP505", "start": "Manali", "end": "Chandigarh", "stops": ["Mandi", "Bilaspur"], "departure": "20:00", "arrival": "07:00", "type": "Volvo AC"},
]

# Insert data into MongoDB
bus_collection.insert_many(buses)

print("Next 10 unique bus records inserted successfully.")
