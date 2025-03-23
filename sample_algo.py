import pymongo
from collections import deque
import re
# MongoDB Connection URI
MONGO_URI = "mongodb://localhost:27017/"
DB_NAME = "travel_app"


def convert_duration_to_minutes(duration_str):
    """Converts duration format '2h 30m' to minutes (150)."""
    match = re.match(r'(?:(\d+)h)?\s*(?:(\d+)m)?', duration_str)
    if match:
        hours = int(match.group(1)) if match.group(1) else 0
        minutes = int(match.group(2)) if match.group(2) else 0
        return hours * 60 + minutes
    return 0  # Default to 0 if format is incorrect

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


def find_routes(graph, start, end):
    """Finds all possible routes from start to end, including intermediate connections."""
    if start not in graph:
        print(f"[INFO] No direct routes found from {start}. Trying indirect paths...")
    
    queue = deque([[{"location": start, "route": None}]])  # BFS Queue
    possible_routes = []

    while queue:
        path = queue.popleft()
        current_location = path[-1]["location"]

        if current_location == end:
            possible_routes.append(path)  # Found a valid route
            continue

        if current_location not in graph:
            continue  # No further connections

        for connection in graph[current_location]:
            new_path = path + [{"location": connection["end"], "route": connection}]
            queue.append(new_path)

    return possible_routes

def find_best_route(graph, start, end, criteria="fastest"):
    """
    Finds the best possible route from start to end based on the given criteria.

    Parameters:
        graph (dict): The transportation graph.
        start (str): Starting location.
        end (str): Destination location.
        criteria (str): The optimization criteria ("fastest", "cheapest", "least_switches").

    Returns:
        list: The best possible route based on the given criteria.
    """
    if start not in graph:
        print(f"[ERROR] No direct or indirect routes found from {start}.")
        return None

    # Priority queue: (cost, duration, switches, path)
    from heapq import heappush, heappop
    pq = []
    heappush(pq, (0, 0, 0, [{"location": start, "route": None}]))  # (cost, duration, switches, path)

    best_route = None
    best_value = float("inf")  # Initialize with high value

    while pq:
        cost, duration, switches, path = heappop(pq)
        current_location = path[-1]["location"]

        if current_location == end:
            if (criteria == "fastest" and duration < best_value) or \
               (criteria == "cheapest" and cost < best_value) or \
               (criteria == "least_switches" and switches < best_value):
                best_route = path
                best_value = min(best_value, duration if criteria == "fastest" else cost if criteria == "cheapest" else switches)

        if current_location not in graph:
            continue

        for connection in graph[current_location]:
            new_path = path + [{"location": connection["destination"], "route": connection}]
            new_cost = cost + connection["details"]["fare"]
            new_duration = duration + connection["details"]["duration"]
            new_switches = switches + 1

            heappush(pq, (new_cost, new_duration, new_switches, new_path))

    return best_route


# Example Call
if __name__ == "__main__":
    trains, buses, cabs, flights = fetch_data()
    graph = build_graph(trains, buses, cabs, flights)

    start_location = "Mumbai"
    end_location = "Delhi"

    best_fastest = find_best_route(graph, start_location, end_location, "fastest")
    best_cheapest = find_best_route(graph, start_location, end_location, "cheapest")
    best_least_switches = find_best_route(graph, start_location, end_location, "least_switches")

    print("\n[INFO] Best Fastest Route:")
    for step in best_fastest:
        if step["route"]:
            print(f"  {step['location']} → ({step['route']['type']}) → ", end="")
    print(end_location)

    print("\n[INFO] Best Cheapest Route:")
    for step in best_cheapest:
        if step["route"]:
            print(f"  {step['location']} → ({step['route']['type']}) → ", end="")
    print(end_location)

    print("\n[INFO] Best Least Switches Route:")
    for step in best_least_switches:
        if step["route"]:
            print(f"  {step['location']} → ({step['route']['type']}) → ", end="")
    print(end_location)

