import pymongo
from datetime import datetime

# Connect to MongoDB
MONGO_URI = "mongodb://localhost:27017/"
client = pymongo.MongoClient(MONGO_URI)
db = client["travel_app"]
train_collection = db["trains"]

# List of 10 train records
trains = [
    {
        "train_number": "12951",
        "train_name": "Mumbai Rajdhani Express",
        "source": "Mumbai Central",
        "destination": "New Delhi",
        "departure_time": datetime(2025, 3, 27, 17, 0),
        "arrival_time": datetime(2025, 3, 28, 8, 35),
        "stops": ["Mumbai Central", "Surat", "Vadodara", "Ratlam", "Kota", "New Delhi"],
        "days_of_operation": ["Monday", "Wednesday", "Friday"],
        "classes": ["AC 3 Tier", "AC 2 Tier", "First AC"],
        "fare": {"AC 3 Tier": 2200, "AC 2 Tier": 3200, "First AC": 4500}
    },
    {
        "train_number": "12625",
        "train_name": "Kerala Express",
        "source": "Trivandrum",
        "destination": "New Delhi",
        "departure_time": datetime(2025, 3, 27, 12, 10),
        "arrival_time": datetime(2025, 3, 29, 13, 15),
        "stops": ["Trivandrum", "Ernakulam", "Coimbatore", "Chennai", "Bhopal", "New Delhi"],
        "days_of_operation": ["Daily"],
        "classes": ["Sleeper", "AC 3 Tier", "AC 2 Tier"],
        "fare": {"Sleeper": 850, "AC 3 Tier": 2200, "AC 2 Tier": 3200}
    },
    {
        "train_number": "12002",
        "train_name": "Bhopal Shatabdi Express",
        "source": "New Delhi",
        "destination": "Bhopal",
        "departure_time": datetime(2025, 3, 27, 6, 0),
        "arrival_time": datetime(2025, 3, 27, 14, 30),
        "stops": ["New Delhi", "Mathura", "Agra", "Gwalior", "Bhopal"],
        "days_of_operation": ["Daily"],
        "classes": ["AC Chair Car", "Executive Class"],
        "fare": {"AC Chair Car": 1500, "Executive Class": 2900}
    },
    {
        "train_number": "18237",
        "train_name": "Chhattisgarh Express",
        "source": "Bilaspur",
        "destination": "Amritsar",
        "departure_time": datetime(2025, 3, 27, 16, 0),
        "arrival_time": datetime(2025, 3, 29, 7, 10),
        "stops": ["Bilaspur", "Raipur", "Nagpur", "Jhansi", "Delhi", "Ludhiana", "Amritsar"],
        "days_of_operation": ["Daily"],
        "classes": ["Sleeper", "AC 3 Tier", "AC 2 Tier"],
        "fare": {"Sleeper": 900, "AC 3 Tier": 2200, "AC 2 Tier": 3100}
    },
    {
        "train_number": "12246",
        "train_name": "Duronto Express",
        "source": "Yesvantpur",
        "destination": "Howrah",
        "departure_time": datetime(2025, 3, 27, 11, 15),
        "arrival_time": datetime(2025, 3, 28, 18, 30),
        "stops": ["Yesvantpur", "Vijayawada", "Visakhapatnam", "Bhubaneswar", "Howrah"],
        "days_of_operation": ["Tuesday", "Friday"],
        "classes": ["AC 3 Tier", "AC 2 Tier", "First AC"],
        "fare": {"AC 3 Tier": 2500, "AC 2 Tier": 3500, "First AC": 5000}
    },
    {
        "train_number": "12138",
        "train_name": "Punjab Mail",
        "source": "Mumbai CST",
        "destination": "Firozpur",
        "departure_time": datetime(2025, 3, 27, 19, 40),
        "arrival_time": datetime(2025, 3, 29, 6, 45),
        "stops": ["Mumbai CST", "Bhusaval", "Bhopal", "Agra", "Delhi", "Firozpur"],
        "days_of_operation": ["Daily"],
        "classes": ["Sleeper", "AC 3 Tier", "AC 2 Tier"],
        "fare": {"Sleeper": 950, "AC 3 Tier": 2300, "AC 2 Tier": 3200}
    },
    {
        "train_number": "12693",
        "train_name": "Pearl City Express",
        "source": "Chennai Egmore",
        "destination": "Tuticorin",
        "departure_time": datetime(2025, 3, 27, 20, 00),
        "arrival_time": datetime(2025, 3, 28, 8, 30),
        "stops": ["Chennai Egmore", "Villupuram", "Madurai", "Tirunelveli", "Tuticorin"],
        "days_of_operation": ["Daily"],
        "classes": ["Sleeper", "AC 3 Tier", "AC 2 Tier"],
        "fare": {"Sleeper": 650, "AC 3 Tier": 1800, "AC 2 Tier": 2700}
    },
    {
        "train_number": "12382",
        "train_name": "Poorva Express",
        "source": "New Delhi",
        "destination": "Howrah",
        "departure_time": datetime(2025, 3, 27, 17, 35),
        "arrival_time": datetime(2025, 3, 28, 16, 00),
        "stops": ["New Delhi", "Kanpur", "Allahabad", "Gaya", "Dhanbad", "Howrah"],
        "days_of_operation": ["Tuesday", "Thursday", "Sunday"],
        "classes": ["Sleeper", "AC 3 Tier", "AC 2 Tier"],
        "fare": {"Sleeper": 1000, "AC 3 Tier": 2400, "AC 2 Tier": 3400}
    },
    {
        "train_number": "12566",
        "train_name": "Bihar Sampark Kranti Express",
        "source": "New Delhi",
        "destination": "Darbhanga",
        "departure_time": datetime(2025, 3, 27, 14, 30),
        "arrival_time": datetime(2025, 3, 28, 12, 00),
        "stops": ["New Delhi", "Kanpur", "Varanasi", "Mokama", "Samastipur", "Darbhanga"],
        "days_of_operation": ["Daily"],
        "classes": ["Sleeper", "AC 3 Tier", "AC 2 Tier"],
        "fare": {"Sleeper": 900, "AC 3 Tier": 2100, "AC 2 Tier": 3100}
    },
    {
        "train_number": "11019",
        "train_name": "Konark Express",
        "source": "Mumbai CST",
        "destination": "Bhubaneswar",
        "departure_time": datetime(2025, 3, 27, 15, 10),
        "arrival_time": datetime(2025, 3, 28, 23, 45),
        "stops": ["Mumbai CST", "Pune", "Solapur", "Vijayawada", "Visakhapatnam", "Bhubaneswar"],
        "days_of_operation": ["Daily"],
        "classes": ["Sleeper", "AC 3 Tier", "AC 2 Tier"],
        "fare": {"Sleeper": 1100, "AC 3 Tier": 2600, "AC 2 Tier": 3600}
    }
]

# Insert Data into MongoDB
train_collection.insert_many(trains)

print("10 Train records inserted successfully!")
