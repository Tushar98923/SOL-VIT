import pymongo

# MongoDB Connection
MONGO_URI = "mongodb://localhost:27017/"
client = pymongo.MongoClient(MONGO_URI)
db = client["travel_app"]
bus_collection = db["buses"]

# Next 10 Unique Bus Records
buses = [
    {"bus_no": "MH102", "start": "Ahmedabad", "end": "Jaipur", "stops": ["Udaipur", "Ajmer"], "departure": "07:00", "arrival": "18:00", "type": "AC Sleeper"},
    {"bus_no": "DL203", "start": "Delhi", "end": "Shimla", "stops": ["Karnal", "Chandigarh", "Solan"], "departure": "06:30", "arrival": "14:00", "type": "Volvo"},
    {"bus_no": "RJ304", "start": "Jaipur", "end": "Agra", "stops": ["Dausa", "Bharatpur"], "departure": "08:15", "arrival": "13:45", "type": "Express"},
    {"bus_no": "UP405", "start": "Lucknow", "end": "Gorakhpur", "stops": ["Faizabad", "Basti"], "departure": "10:00", "arrival": "15:00", "type": "Luxury"},
    {"bus_no": "WB506", "start": "Kolkata", "end": "Digha", "stops": ["Kharagpur", "Contai"], "departure": "07:30", "arrival": "11:30", "type": "AC Seater"},
    {"bus_no": "TN607", "start": "Chennai", "end": "Pondicherry", "stops": ["Mahabalipuram"], "departure": "09:00", "arrival": "12:00", "type": "AC Seater"},
    {"bus_no": "KA708", "start": "Bangalore", "end": "Coorg", "stops": ["Mysore", "Kushalnagar"], "departure": "05:45", "arrival": "12:30", "type": "Luxury"},
    {"bus_no": "KL809", "start": "Kochi", "end": "Munnar", "stops": ["Aluva", "Adimali"], "departure": "08:00", "arrival": "13:00", "type": "Express"},
    {"bus_no": "MP910", "start": "Bhopal", "end": "Indore", "stops": ["Sehore", "Dewas"], "departure": "09:30", "arrival": "12:30", "type": "AC Sleeper"},
    {"bus_no": "CG011", "start": "Raipur", "end": "Bilaspur", "stops": ["Tilda", "Bhatapara"], "departure": "07:00", "arrival": "11:00", "type": "Luxury"}
]

# Insert into MongoDB
bus_collection.insert_many(buses)

print("Next 10 buses inserted successfully!")
