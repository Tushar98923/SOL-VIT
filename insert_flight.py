import pymongo

# MongoDB Connection
MONGO_URI = "mongodb://localhost:27017/"
client = pymongo.MongoClient(MONGO_URI)
db = client["travel_app"]
flight_collection = db["flights"]

# Flight Data
flights = [
    {"flight_no": "AI101", "airline": "Air India", "from": "DEL", "to": "BOM", "departure": "08:00", "arrival": "10:30", "duration": "2h 30m", "price": 5500},
    {"flight_no": "6E202", "airline": "IndiGo", "from": "BOM", "to": "BLR", "departure": "09:45", "arrival": "12:15", "duration": "2h 30m", "price": 4700},
    {"flight_no": "SG303", "airline": "SpiceJet", "from": "BLR", "to": "HYD", "departure": "07:15", "arrival": "08:45", "duration": "1h 30m", "price": 3800},
    {"flight_no": "UK404", "airline": "Vistara", "from": "HYD", "to": "MAA", "departure": "14:00", "arrival": "15:30", "duration": "1h 30m", "price": 4200},
    {"flight_no": "G8305", "airline": "Go First", "from": "MAA", "to": "DEL", "departure": "18:30", "arrival": "21:15", "duration": "2h 45m", "price": 6000},
    {"flight_no": "AI502", "airline": "Air India", "from": "DEL", "to": "CCU", "departure": "11:00", "arrival": "13:15", "duration": "2h 15m", "price": 5300},
    {"flight_no": "6E703", "airline": "IndiGo", "from": "CCU", "to": "IXB", "departure": "10:00", "arrival": "11:30", "duration": "1h 30m", "price": 3700},
    {"flight_no": "SG808", "airline": "SpiceJet", "from": "IXB", "to": "GAU", "departure": "12:45", "arrival": "14:00", "duration": "1h 15m", "price": 3300},
    {"flight_no": "UK909", "airline": "Vistara", "from": "GAU", "to": "IMF", "departure": "15:30", "arrival": "17:00", "duration": "1h 30m", "price": 4200},
    {"flight_no": "AI111", "airline": "Air India", "from": "IMF", "to": "DEL", "departure": "19:30", "arrival": "22:15", "duration": "2h 45m", "price": 6500},
    {"flight_no": "6E505", "airline": "IndiGo", "from": "DEL", "to": "PNQ", "departure": "06:30", "arrival": "08:45", "duration": "2h 15m", "price": 4800},
    {"flight_no": "SG606", "airline": "SpiceJet", "from": "PNQ", "to": "GOI", "departure": "12:00", "arrival": "13:30", "duration": "1h 30m", "price": 3700},
    {"flight_no": "UK707", "airline": "Vistara", "from": "GOI", "to": "HYD", "departure": "15:45", "arrival": "17:30", "duration": "1h 45m", "price": 4200},
    {"flight_no": "G8202", "airline": "Go First", "from": "HYD", "to": "BLR", "departure": "20:00", "arrival": "21:15", "duration": "1h 15m", "price": 3500},
    {"flight_no": "AI303", "airline": "Air India", "from": "BLR", "to": "TRV", "departure": "07:45", "arrival": "09:30", "duration": "1h 45m", "price": 3900},
    {"flight_no": "6E404", "airline": "IndiGo", "from": "TRV", "to": "COK", "departure": "10:15", "arrival": "11:30", "duration": "1h 15m", "price": 3200},
    {"flight_no": "SG909", "airline": "SpiceJet", "from": "COK", "to": "DEL", "departure": "18:30", "arrival": "21:15", "duration": "2h 45m", "price": 5800},
    {"flight_no": "UK505", "airline": "Vistara", "from": "DEL", "to": "JAI", "departure": "07:30", "arrival": "08:45", "duration": "1h 15m", "price": 3200},
    {"flight_no": "AI808", "airline": "Air India", "from": "JAI", "to": "BOM", "departure": "14:00", "arrival": "16:00", "duration": "2h 00m", "price": 4900},
]

# Insert into MongoDB
flight_collection.insert_many(flights)

print("20 Flights inserted successfully!")
