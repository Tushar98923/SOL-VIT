import pymongo

# MongoDB Connection
MONGO_URI = "mongodb://localhost:27017/"
client = pymongo.MongoClient(MONGO_URI)
db = client["travel_app"]
bus_collection = db["buses"]

# Next 10 Unique Bus Records
buses = [
    {"bus_no": "AP01", "operator": "Airport Express", "from": "Delhi Railway Station", "to": "IGI Airport", "stops": ["CP", "RK Ashram"], "departure": "05:00", "arrival": "05:45", "fare": 150},
    {"bus_no": "AP02", "operator": "Delhi Metro Feeder", "from": "New Delhi Station", "to": "IGI Airport", "stops": ["Aerocity"], "departure": "06:30", "arrival": "07:00", "fare": 100},
    {"bus_no": "AP03", "operator": "BEST", "from": "Mumbai Central", "to": "CSIA Mumbai", "stops": ["Dadar", "Andheri"], "departure": "07:15", "arrival": "08:00", "fare": 180},
    {"bus_no": "AP04", "operator": "KSRTC", "from": "Bangalore City Station", "to": "Kempegowda Airport", "stops": ["Hebbal"], "departure": "08:00", "arrival": "09:15", "fare": 200},
    {"bus_no": "AP05", "operator": "TSRTC", "from": "Hyderabad Deccan Station", "to": "Rajiv Gandhi Airport", "stops": ["Mehdipatnam"], "departure": "09:30", "arrival": "10:20", "fare": 150},
    {"bus_no": "AP06", "operator": "TNSTC", "from": "Chennai Central", "to": "Chennai Airport", "stops": ["Guindy"], "departure": "10:45", "arrival": "11:15", "fare": 100},
    {"bus_no": "AP07", "operator": "WBTC", "from": "Howrah Station", "to": "Netaji Subhash Airport", "stops": ["Dumdum"], "departure": "12:00", "arrival": "12:45", "fare": 120},
    {"bus_no": "AP08", "operator": "GSRTC", "from": "Ahmedabad Junction", "to": "Sardar Vallabhbhai Patel Airport", "stops": ["Naranpura"], "departure": "13:30", "arrival": "14:00", "fare": 130},
    {"bus_no": "AP09", "operator": "PMPML", "from": "Pune Railway Station", "to": "Pune Airport", "stops": ["Viman Nagar"], "departure": "14:30", "arrival": "15:00", "fare": 110},
    {"bus_no": "AP10", "operator": "BMTC", "from": "Mysore Railway Station", "to": "Kempegowda Airport", "stops": ["Mandya", "Electronic City"], "departure": "15:30", "arrival": "18:00", "fare": 250},
]

# Insert data into MongoDB
bus_collection.insert_many(buses)

print("Next 10 unique bus records inserted successfully.")
