import pymongo

# MongoDB Connection
MONGO_URI = "mongodb://localhost:27017/"
client = pymongo.MongoClient(MONGO_URI)
db = client["travel_app"]
bus_collection = db["buses"]

# Next 10 Unique Bus Records
buses = [
    {"bus_no": "AP707", "start": "Hyderabad", "end": "Vijayawada", "stops": ["Nalgonda"], "departure": "09:00", "arrival": "14:00", "type": "Luxury AC"},
    {"bus_no": "TN808", "start": "Chennai", "end": "Madurai", "stops": ["Villupuram", "Trichy"], "departure": "22:00", "arrival": "06:30", "type": "Sleeper AC"},
    {"bus_no": "GJ909", "start": "Rajkot", "end": "Bhavnagar", "stops": ["Gondal", "Botad"], "departure": "15:30", "arrival": "20:00", "type": "Volvo AC"},
    {"bus_no": "WB101", "start": "Siliguri", "end": "Darjeeling", "stops": ["Kurseong"], "departure": "07:00", "arrival": "11:00", "type": "AC Seater"},
    {"bus_no": "UP202", "start": "Agra", "end": "Kanpur", "stops": ["Etawah"], "departure": "17:00", "arrival": "22:30", "type": "Deluxe"},
    {"bus_no": "MH303", "start": "Mumbai", "end": "Shirdi", "stops": ["Nashik"], "departure": "23:30", "arrival": "07:00", "type": "Sleeper"},
    {"bus_no": "RJ404", "start": "Jodhpur", "end": "Bikaner", "stops": ["Nagaur"], "departure": "05:30", "arrival": "12:00", "type": "Luxury AC"},
    {"bus_no": "BR505", "start": "Muzaffarpur", "end": "Darbhanga", "stops": ["Samastipur"], "departure": "10:00", "arrival": "13:30", "type": "Deluxe"},
    {"bus_no": "JK606", "start": "Leh", "end": "Kargil", "stops": ["Lamayuru"], "departure": "06:00", "arrival": "14:30", "type": "AC Seater"},
    {"bus_no": "MP707", "start": "Indore", "end": "Bhopal", "stops": ["Ujjain"], "departure": "18:30", "arrival": "22:00", "type": "Volvo AC"},
]

# Insert data into MongoDB
bus_collection.insert_many(buses)

print("Next 10 unique bus records inserted successfully.")
