import pymongo
import re
from collections import deque

# MongoDB Connection URI
MONGO_URI = "mongodb://localhost:27017/"
DB_NAME = "travel_app"

### 1️⃣ CONVERT DURATION TO MINUTES ###
def convert_duration_to_minutes(duration_str):
    """Converts duration format '2h 30m' to minutes (150)."""
    if not duration_str:
        return 0  # Handle missing durations
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
            flight["fare"] = flight.pop("price", 0)  # Rename 'price' to 'fare', default 0
            flight["duration"] = convert_duration_to_minutes(flight.get("duration", "0h"))  # Convert duration

        client.close()  # Close MongoDB connection

        print(f"[DEBUG] Fetched {len(train_data)} trains from database.")
        print(f"[DEBUG] Fetched {len(bus_data)} buses from database.")
        print(f"[DEBUG] Fetched {len(cab_data)} cabs from database.")
        print(f"[DEBUG] Fetched {len(flight_data)} flights from database.")

        return train_data, bus_data, cab_data, flight_data

    except pymongo.errors.ConnectionError:
        print("[ERROR] Could not connect to MongoDB. Is the server running?")
    except pymongo.errors.PyMongoError as e:
        print(f"[ERROR] MongoDB Query Failed: {e}")
    except Exception as e:
        print(f"[ERROR] Unexpected Error: {e}")

    return [], [], [], []  # Return empty lists if an error occurs

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

    # Add all routes
    for transport_data, transport_type in [(trains, "Train"), (buses, "Bus"), (cabs, "Cab"), (flights, "Flight")]:
        for transport in transport_data:
            add_route(transport.get("source"), transport.get("destination"), transport_type, transport)

    return graph

### 4️⃣ FIND BEST ROUTES ###
def find_routes(graph, start, end, preference="cheapest"):
    """Finds the best possible route based on user preference (cheapest, fastest, least switches)."""
    if start not in graph:
        print(f"[ERROR] No routes found from {start}.")
        return None

    queue = deque([[{"location": start, "route": None, "cost": 0, "time": 0, "switches": 0}]])  # BFS Queue
    best_route = None

    while queue:
        path = queue.popleft()
        current_location = path[-1]["location"]
        total_cost = path[-1]["cost"]
        total_time = path[-1]["time"]
        total_switches = path[-1]["switches"]

        if current_location == end:
            if not best_route or is_better_route(path, best_route, preference):
                best_route = path  # Update the best route
            continue

        if current_location not in graph:
            continue  # No further connections

        for connection in graph[current_location]:
            details = connection["details"]
            cost = details.get("fare", 0)
            time = details.get("duration", 0)

            new_path = path + [{
                "location": connection["destination"],
                "route": connection,
                "cost": total_cost + cost,
                "time": total_time + time,
                "switches": total_switches + 1
            }]
            queue.append(new_path)

    return best_route

### 5️⃣ COMPARE ROUTES BASED ON USER PREFERENCE ###
def is_better_route(new_route, best_route, preference):
    """Compares two routes based on the user's preference."""
    if preference == "cheapest":
        return new_route[-1]["cost"] < best_route[-1]["cost"]
    elif preference == "fastest":
        return new_route[-1]["time"] < best_route[-1]["time"]
    elif preference == "least_switches":
        return new_route[-1]["switches"] < best_route[-1]["switches"]
    return False  # Default case

### 6️⃣ RUN THE PROGRAM ###
if __name__ == "__main__":
    trains, buses, cabs, flights = fetch_data()
    graph = build_graph(trains, buses, cabs, flights)

    start_location = "Mumbai"
    end_location = "Delhi"
    preference = "cheapest"  # Change to "fastest" or "least_switches"

    best_route = find_routes(graph, start_location, end_location, preference)

    if best_route:
        print(f"\n[INFO] Best {preference.capitalize()} Route:")
        route_display = "  " + " → ".join(
            f"{step['location']} ({step['route']['type']})"
            for step in best_route if step["route"]
        )
        print(route_display)
    else:
        print(f"[ERROR] No valid routes found from {start_location} to {end_location}.")
