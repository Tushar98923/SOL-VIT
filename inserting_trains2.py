import pymongo
from datetime import datetime

# Connect to MongoDB
MONGO_URI = "mongodb://localhost:27017/"
client = pymongo.MongoClient(MONGO_URI)
db = client["travel_app"]
train_collection = db["trains"]
# List of next 10 train records
trains = [
    {
        "train_number": "12431",
        "train_name": "Rajdhani Express",
        "source": "Thiruvananthapuram",
        "destination": "H. Nizamuddin",
        "departure_time": datetime(2025, 3, 27, 19, 15),
        "arrival_time": datetime(2025, 3, 29, 5, 45),
        "stops": ["Thiruvananthapuram", "Kollam", "Ernakulam", "Bhopal", "Nizamuddin"],
        "days_of_operation": ["Monday", "Thursday"],
        "classes": ["AC 3 Tier", "AC 2 Tier", "First AC"],
        "fare": {"AC 3 Tier": 3200, "AC 2 Tier": 4500, "First AC": 6500}
    },
    {
        "train_number": "12801",
        "train_name": "Puri New Delhi Express",
        "source": "Puri",
        "destination": "New Delhi",
        "departure_time": datetime(2025, 3, 27, 22, 55),
        "arrival_time": datetime(2025, 3, 29, 7, 30),
        "stops": ["Puri", "Bhubaneswar", "Kharagpur", "Allahabad", "Kanpur", "New Delhi"],
        "days_of_operation": ["Wednesday", "Saturday"],
        "classes": ["Sleeper", "AC 3 Tier", "AC 2 Tier"],
        "fare": {"Sleeper": 1100, "AC 3 Tier": 2900, "AC 2 Tier": 4000}
    },
    {
        "train_number": "12296",
        "train_name": "Sanghamitra Express",
        "source": "Bangalore",
        "destination": "Patna",
        "departure_time": datetime(2025, 3, 27, 9, 00),
        "arrival_time": datetime(2025, 3, 29, 11, 30),
        "stops": ["Bangalore", "Chennai", "Vijayawada", "Nagpur", "Mughalsarai", "Patna"],
        "days_of_operation": ["Daily"],
        "classes": ["Sleeper", "AC 3 Tier", "AC 2 Tier"],
        "fare": {"Sleeper": 1200, "AC 3 Tier": 3100, "AC 2 Tier": 4200}
    },
    {
        "train_number": "11077",
        "train_name": "Jhelum Express",
        "source": "Pune",
        "destination": "Jammu Tawi",
        "departure_time": datetime(2025, 3, 27, 17, 20),
        "arrival_time": datetime(2025, 3, 29, 11, 10),
        "stops": ["Pune", "Manmad", "Bhopal", "Agra", "New Delhi", "Ludhiana", "Jammu Tawi"],
        "days_of_operation": ["Daily"],
        "classes": ["Sleeper", "AC 3 Tier", "AC 2 Tier"],
        "fare": {"Sleeper": 1300, "AC 3 Tier": 3400, "AC 2 Tier": 4600}
    },
    {
        "train_number": "12322",
        "train_name": "Kolkata Mail",
        "source": "Mumbai CST",
        "destination": "Howrah",
        "departure_time": datetime(2025, 3, 27, 21, 25),
        "arrival_time": datetime(2025, 3, 29, 3, 55),
        "stops": ["Mumbai CST", "Bhusaval", "Nagpur", "Bilaspur", "Kharagpur", "Howrah"],
        "days_of_operation": ["Daily"],
        "classes": ["Sleeper", "AC 3 Tier", "AC 2 Tier"],
        "fare": {"Sleeper": 1200, "AC 3 Tier": 3200, "AC 2 Tier": 4400}
    },
    {
        "train_number": "16587",
        "train_name": "Bikaner Express",
        "source": "Yeshvantpur",
        "destination": "Bikaner",
        "departure_time": datetime(2025, 3, 27, 22, 15),
        "arrival_time": datetime(2025, 3, 29, 14, 45),
        "stops": ["Yeshvantpur", "Hubli", "Pune", "Ahmedabad", "Jaipur", "Bikaner"],
        "days_of_operation": ["Tuesday", "Friday"],
        "classes": ["Sleeper", "AC 3 Tier", "AC 2 Tier"],
        "fare": {"Sleeper": 1400, "AC 3 Tier": 3500, "AC 2 Tier": 4700}
    },
    {
        "train_number": "12723",
        "train_name": "Telangana Express",
        "source": "Hyderabad",
        "destination": "New Delhi",
        "departure_time": datetime(2025, 3, 27, 6, 25),
        "arrival_time": datetime(2025, 3, 28, 7, 5),
        "stops": ["Hyderabad", "Kazipet", "Nagpur", "Bhopal", "Jhansi", "New Delhi"],
        "days_of_operation": ["Daily"],
        "classes": ["Sleeper", "AC 3 Tier", "AC 2 Tier"],
        "fare": {"Sleeper": 1150, "AC 3 Tier": 3000, "AC 2 Tier": 4100}
    },
    {
        "train_number": "12141",
        "train_name": "Rajendranagar Express",
        "source": "Mumbai CST",
        "destination": "Patna",
        "departure_time": datetime(2025, 3, 27, 23, 30),
        "arrival_time": datetime(2025, 3, 29, 5, 10),
        "stops": ["Mumbai CST", "Bhusaval", "Igatpuri", "Jabalpur", "Patna"],
        "days_of_operation": ["Daily"],
        "classes": ["Sleeper", "AC 3 Tier", "AC 2 Tier"],
        "fare": {"Sleeper": 1100, "AC 3 Tier": 2800, "AC 2 Tier": 3900}
    },
    {
        "train_number": "12413",
        "train_name": "Pooja Express",
        "source": "Ajmer",
        "destination": "Jammu Tawi",
        "departure_time": datetime(2025, 3, 27, 14, 5),
        "arrival_time": datetime(2025, 3, 28, 7, 15),
        "stops": ["Ajmer", "Jaipur", "New Delhi", "Ludhiana", "Jammu Tawi"],
        "days_of_operation": ["Daily"],
        "classes": ["Sleeper", "AC 3 Tier", "AC 2 Tier"],
        "fare": {"Sleeper": 950, "AC 3 Tier": 2500, "AC 2 Tier": 3600}
    },
    {
        "train_number": "11027",
        "train_name": "Chennai Mail",
        "source": "Mumbai CST",
        "destination": "Chennai Central",
        "departure_time": datetime(2025, 3, 27, 12, 45),
        "arrival_time": datetime(2025, 3, 28, 16, 35),
        "stops": ["Mumbai CST", "Pune", "Solapur", "Guntakal", "Chennai Central"],
        "days_of_operation": ["Daily"],
        "classes": ["Sleeper", "AC 3 Tier", "AC 2 Tier"],
        "fare": {"Sleeper": 1000, "AC 3 Tier": 2700, "AC 2 Tier": 3800}
    }
]

# Insert Data into MongoDB
train_collection.insert_many(trains)

print("Next 10 Train records inserted successfully!")
