import pymongo
from datetime import datetime

# Connect to MongoDB
MONGO_URI = "mongodb://localhost:27017/"
client = pymongo.MongoClient(MONGO_URI)
db = client["travel_app"]
train_collection = db["trains"]
# Next 10 train records
trains = [
    {
        "train_number": "12649",
        "train_name": "Karnataka Sampark Kranti Express",
        "source": "Bangalore",
        "destination": "New Delhi",
        "departure_time": datetime(2025, 3, 27, 13, 40),
        "arrival_time": datetime(2025, 3, 28, 20, 45),
        "stops": ["Bangalore", "Dharmavaram", "Nagpur", "Bhopal", "Jhansi", "New Delhi"],
        "days_of_operation": ["Monday", "Thursday"],
        "classes": ["Sleeper", "AC 3 Tier", "AC 2 Tier"],
        "fare": {"Sleeper": 1250, "AC 3 Tier": 3100, "AC 2 Tier": 4200}
    },
    {
        "train_number": "12506",
        "train_name": "North East Express",
        "source": "Guwahati",
        "destination": "Anand Vihar Terminal",
        "departure_time": datetime(2025, 3, 27, 7, 30),
        "arrival_time": datetime(2025, 3, 28, 18, 55),
        "stops": ["Guwahati", "New Jalpaiguri", "Patna", "Kanpur", "Anand Vihar Terminal"],
        "days_of_operation": ["Daily"],
        "classes": ["Sleeper", "AC 3 Tier", "AC 2 Tier"],
        "fare": {"Sleeper": 1350, "AC 3 Tier": 3300, "AC 2 Tier": 4400}
    },
    {
        "train_number": "22691",
        "train_name": "KSR Bengaluru - Hazrat Nizamuddin Rajdhani Express",
        "source": "Bangalore",
        "destination": "H. Nizamuddin",
        "departure_time": datetime(2025, 3, 27, 20, 00),
        "arrival_time": datetime(2025, 3, 29, 5, 55),
        "stops": ["Bangalore", "Hubli", "Vijayawada", "Nagpur", "Bhopal", "Nizamuddin"],
        "days_of_operation": ["Wednesday", "Sunday"],
        "classes": ["AC 3 Tier", "AC 2 Tier", "First AC"],
        "fare": {"AC 3 Tier": 3400, "AC 2 Tier": 4600, "First AC": 7000}
    },
    {
        "train_number": "12050",
        "train_name": "Gatiman Express",
        "source": "New Delhi",
        "destination": "Jhansi",
        "departure_time": datetime(2025, 3, 27, 8, 10),
        "arrival_time": datetime(2025, 3, 27, 12, 35),
        "stops": ["New Delhi", "Agra", "Gwalior", "Jhansi"],
        "days_of_operation": ["Daily"],
        "classes": ["AC Chair Car", "Executive Chair Car"],
        "fare": {"AC Chair Car": 1500, "Executive Chair Car": 2800}
    },
    {
        "train_number": "22672",
        "train_name": "Madurai Express",
        "source": "Chennai Egmore",
        "destination": "Madurai",
        "departure_time": datetime(2025, 3, 27, 22, 10),
        "arrival_time": datetime(2025, 3, 28, 6, 15),
        "stops": ["Chennai Egmore", "Villupuram", "Trichy", "Dindigul", "Madurai"],
        "days_of_operation": ["Daily"],
        "classes": ["Sleeper", "AC 3 Tier", "AC 2 Tier"],
        "fare": {"Sleeper": 700, "AC 3 Tier": 1800, "AC 2 Tier": 2700}
    },
    {
        "train_number": "11019",
        "train_name": "Konark Express",
        "source": "Mumbai CST",
        "destination": "Bhubaneswar",
        "departure_time": datetime(2025, 3, 27, 15, 5),
        "arrival_time": datetime(2025, 3, 28, 23, 40),
        "stops": ["Mumbai CST", "Pune", "Solapur", "Nagpur", "Raipur", "Bhubaneswar"],
        "days_of_operation": ["Daily"],
        "classes": ["Sleeper", "AC 3 Tier", "AC 2 Tier"],
        "fare": {"Sleeper": 1400, "AC 3 Tier": 3200, "AC 2 Tier": 4300}
    },
    {
        "train_number": "12453",
        "train_name": "Ranchi Rajdhani Express",
        "source": "Ranchi",
        "destination": "New Delhi",
        "departure_time": datetime(2025, 3, 27, 17, 15),
        "arrival_time": datetime(2025, 3, 28, 11, 10),
        "stops": ["Ranchi", "Bokaro", "Gaya", "Allahabad", "Kanpur", "New Delhi"],
        "days_of_operation": ["Monday", "Thursday"],
        "classes": ["AC 3 Tier", "AC 2 Tier", "First AC"],
        "fare": {"AC 3 Tier": 3100, "AC 2 Tier": 4300, "First AC": 6700}
    },
    {
        "train_number": "12688",
        "train_name": "Dehradun Express",
        "source": "Madurai",
        "destination": "Dehradun",
        "departure_time": datetime(2025, 3, 27, 23, 35),
        "arrival_time": datetime(2025, 3, 30, 10, 30),
        "stops": ["Madurai", "Trichy", "Chennai", "Nagpur", "Jhansi", "New Delhi", "Dehradun"],
        "days_of_operation": ["Wednesday", "Saturday"],
        "classes": ["Sleeper", "AC 3 Tier", "AC 2 Tier"],
        "fare": {"Sleeper": 2200, "AC 3 Tier": 5200, "AC 2 Tier": 7200}
    },
    {
        "train_number": "12716",
        "train_name": "Sachkhand Express",
        "source": "Huzur Sahib Nanded",
        "destination": "Amritsar",
        "departure_time": datetime(2025, 3, 27, 9, 30),
        "arrival_time": datetime(2025, 3, 28, 18, 45),
        "stops": ["Nanded", "Aurangabad", "Bhopal", "New Delhi", "Ludhiana", "Amritsar"],
        "days_of_operation": ["Daily"],
        "classes": ["Sleeper", "AC 3 Tier", "AC 2 Tier"],
        "fare": {"Sleeper": 1500, "AC 3 Tier": 3700, "AC 2 Tier": 4900}
    },
    {
        "train_number": "12217",
        "train_name": "Kerala Sampark Kranti Express",
        "source": "Kochuveli",
        "destination": "Chandigarh",
        "departure_time": datetime(2025, 3, 27, 8, 50),
        "arrival_time": datetime(2025, 3, 29, 16, 30),
        "stops": ["Kochuveli", "Ernakulam", "Madgaon", "Vadodara", "New Delhi", "Chandigarh"],
        "days_of_operation": ["Tuesday", "Friday"],
        "classes": ["Sleeper", "AC 3 Tier", "AC 2 Tier"],
        "fare": {"Sleeper": 2400, "AC 3 Tier": 6200, "AC 2 Tier": 8500}
    }
]

# Insert Data into MongoDB
train_collection.insert_many(trains)

print("Next 10 Train records inserted successfully!")

