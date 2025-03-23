import pymongo

# MongoDB Connection
MONGO_URI = "mongodb://localhost:27017/"
client = pymongo.MongoClient(MONGO_URI)
db = client["travel_app"]
cab_collection = db["cabs"]

# Next 20 Unique Cabs
cabs = [
    {"cab_id": "CAB101", "operator": "Uber", "from": "Delhi Railway Station", "to": "IGI Airport", "fare": 600, "type": "Sedan"},
    {"cab_id": "CAB102", "operator": "Ola", "from": "New Delhi Station", "to": "IGI Airport", "fare": 550, "type": "Hatchback"},
    {"cab_id": "CAB103", "operator": "Meru", "from": "Mumbai Central", "to": "CSIA Mumbai", "fare": 700, "type": "SUV"},
    {"cab_id": "CAB104", "operator": "Uber", "from": "Bangalore City Station", "to": "Kempegowda Airport", "fare": 850, "type": "Sedan"},
    {"cab_id": "CAB105", "operator": "Ola", "from": "Hyderabad Deccan Station", "to": "Rajiv Gandhi Airport", "fare": 750, "type": "SUV"},
    {"cab_id": "CAB106", "operator": "Meru", "from": "Chennai Central", "to": "Chennai Airport", "fare": 500, "type": "Hatchback"},
    {"cab_id": "CAB107", "operator": "Uber", "from": "Howrah Station", "to": "Netaji Subhash Airport", "fare": 650, "type": "Sedan"},
    {"cab_id": "CAB108", "operator": "Ola", "from": "Ahmedabad Junction", "to": "Sardar Vallabhbhai Patel Airport", "fare": 600, "type": "SUV"},
    {"cab_id": "CAB109", "operator": "Meru", "from": "Pune Railway Station", "to": "Pune Airport", "fare": 500, "type": "Hatchback"},
    {"cab_id": "CAB110", "operator": "Uber", "from": "Mysore Railway Station", "to": "Kempegowda Airport", "fare": 1200, "type": "Luxury"},
    {"cab_id": "CAB111", "operator": "Ola", "from": "Jaipur Railway Station", "to": "Jaipur Airport", "fare": 700, "type": "Sedan"},
    {"cab_id": "CAB112", "operator": "Meru", "from": "Lucknow Charbagh", "to": "Lucknow Airport", "fare": 650, "type": "SUV"},
    {"cab_id": "CAB113", "operator": "Uber", "from": "Kochi Railway Station", "to": "Cochin Airport", "fare": 750, "type": "Luxury"},
    {"cab_id": "CAB114", "operator": "Ola", "from": "Bhopal Railway Station", "to": "Bhopal Airport", "fare": 550, "type": "Hatchback"},
    {"cab_id": "CAB115", "operator": "Meru", "from": "Indore Junction", "to": "Indore Airport", "fare": 600, "type": "Sedan"},
    {"cab_id": "CAB116", "operator": "Uber", "from": "Trivandrum Railway Station", "to": "Trivandrum Airport", "fare": 800, "type": "Luxury"},
    {"cab_id": "CAB117", "operator": "Ola", "from": "Goa Madgaon Station", "to": "Dabolim Airport", "fare": 650, "type": "SUV"},
    {"cab_id": "CAB118", "operator": "Meru", "from": "Varanasi Railway Station", "to": "Lal Bahadur Shastri Airport", "fare": 700, "type": "Sedan"},
    {"cab_id": "CAB119", "operator": "Uber", "from": "Patna Railway Station", "to": "Jay Prakash Narayan Airport", "fare": 600, "type": "Hatchback"},
    {"cab_id": "CAB120", "operator": "Ola", "from": "Guwahati Railway Station", "to": "Lokpriya Gopinath Airport", "fare": 750, "type": "SUV"},
]

# Insert data into MongoDB
cab_collection.insert_many(cabs)

print("Next 20 unique cab records inserted successfully.")
