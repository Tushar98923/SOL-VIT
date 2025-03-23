import pymongo
import re

# MongoDB Connection URI
MONGO_URI = "mongodb://localhost:27017/"
DB_NAME = "travel_app"

### 1️⃣ CONVERT DURATION TO MINUTES ###
def convert_duration_to_minutes(duration_str):
    """Converts duration format '2h 30m' to minutes (150)."""
    match = re.match(r'(?:(\d+)h)?\s*(?:(\d+)m)?', duration_str)
    if match:
        hours = int(match.group(1)) if match.group(1) else 0
        minutes = int(match.group(2)) if match.group(2) else 0
        return hours * 60 + minutes
    return 0  # Default to 0 if format is incorrect

### 2️⃣ FETCH DATA FROM DATABASE ###
def fetch_data():
    """Fetches all transportation data from MongoDB and ensures proper field names."""
    try:
        client = pymongo.MongoClient(MONGO_URI)
        db = client[DB_NAME]

        train_data = list(db["trains"].find({}))
        bus_data = list(db["buses"].find({}))
        cab_data = list(db["cabs"].find({}))
        flight_data = list(db["flights"].find({}))

        # Convert flight data field names
        for flight in flight_data:
            flight["source"] = flight.pop("from", None)  # Rename 'from' to 'source'
            flight["destination"] = flight.pop("to", None)  # Rename 'to' to 'destination'
            flight["fare"] = flight.pop("price", None)  # Rename 'price' to 'fare'
            flight["duration"] = convert_duration_to_minutes(flight["duration"])  # Convert duration to minutes

        return train_data, bus_data, cab_data, flight_data

    except pymongo.errors.ConnectionError:
        print("[ERROR] Could not connect to MongoDB. Is the server running?")
    except pymongo.errors.PyMongoError as e:
        print(f"[ERROR] MongoDB Query Failed: {e}")
    except Exception as e:
        print(f"[ERROR] Unexpected Error: {e}")

    return [], [], [], []  # ✅ Always return empty lists instead of None

### 3️⃣ BUILD GRAPH ###
def build_graph(trains, buses, cabs, flights):
    """Builds a graph from all transportation data."""
    graph = {}

    def add_route(source, destination, transport_type, details):
        """Adds a route to the graph with transport details."""
        if not source or not destination:
            print(f"[WARNING] Skipping {transport_type} record with missing data: {details}")
            return  # Skip this entry if source or destination is missing

        if source not in graph:
            graph[source] = []
        graph[source].append({"destination": destination, "type": transport_type, "details": details})

    # Add all train routes
    for train in trains:
        add_route(train.get("source"), train.get("destination"), "Train", train)

    # Add all bus routes
    for bus in buses:
        add_route(bus.get("source"), bus.get("destination"), "Bus", bus)

    # Add all cab routes
    for cab in cabs:
        add_route(cab.get("source"), cab.get("destination"), "Cab", cab)

    # Add all flight routes
    for flight in flights:
        add_route(flight.get("source"), flight.get("destination"), "Flight", flight)

    return graph

### 4️⃣ TEST BUILD GRAPH ###
if __name__ == "__main__":
    trains, buses, cabs, flights = fetch_data()
    graph = build_graph(trains, buses, cabs, flights)

    # ✅ Print the graph for verification
    print("\n--- GRAPH DATA ---")
    for source, connections in graph.items():
        print(f"{source}:")
        for connection in connections:
            destination = connection["destination"]
            transport_type = connection["type"]
            details = connection["details"]
            print(f"  → {destination} via {transport_type} | Fare: {details.get('fare', 'N/A')} | Duration: {details.get('duration', 'N/A')} min")
