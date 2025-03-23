from pymongo import MongoClient
from datetime import datetime, timedelta


class RouteFinder:
    def __init__(self):
        self.graph = {}
        self.sources = set()
        self.destinations = set()

    def add_route(self, source, destination, mode, cost, duration):
        """Add route to the graph with multiple modes and options."""
        if source not in self.graph:
            self.graph[source] = {}
        if destination not in self.graph[source]:
            self.graph[source][destination] = []
        self.graph[source][destination].append({
            "mode": mode,
            "cost": cost,
            "duration": duration
        })
        # Track unique sources and destinations
        self.sources.add(source)
        self.destinations.add(destination)

    def fetch_data(self):
        """Fetch data from MongoDB and build graph."""
        client = MongoClient('mongodb://localhost:27017/')
        db = client["travel_app"]

        # Fetch all collections
        flight_data = list(db["flights"].find())
        bus_data = list(db["buses"].find())
        train_data = list(db["trains"].find())
        cab_data = list(db["cabs"].find())

        # Standardize field names
        self.standardize_data(flight_data, "flight")
        self.standardize_data(bus_data, "bus")
        self.standardize_data(train_data, "train")
        self.standardize_data(cab_data, "cab")

        # Debug: Check if graph is populated correctly
        if not self.graph:
            print("[WARNING] Graph is empty. Check data fetching and field renaming.")

    def standardize_data(self, data, mode):
        """Standardize field names across all modes."""
        for record in data:
            if mode == "flight" or mode == "cab":
                record["source"] = record.pop("from", None)
                record["destination"] = record.pop("to", None)
            elif mode == "bus":
                record["source"] = record.pop("start", None)
                record["destination"] = record.pop("end", None)

            # Calculate duration for trains if needed
            if mode == "train" and "departure_time" in record and "arrival_time" in record:
                duration = record["arrival_time"] - record["departure_time"]
                record["duration"] = int(duration.total_seconds() / 60)

            # Add valid records to graph
            if "source" in record and "destination" in record and "cost" in record and "duration" in record:
                self.add_route(
                    record["source"],
                    record["destination"],
                    mode,
                    record["cost"],
                    record["duration"]
                )
            else:
                print(f"[ERROR] Missing data in record: {record}")

    def get_routes(self, source, destination):
        """Retrieve possible routes from source to destination."""
        if source in self.graph and destination in self.graph[source]:
            return self.graph[source][destination]
        else:
            return []

    def print_graph(self):
        """Debug function to print the graph."""
        for source, destinations in self.graph.items():
            for destination, routes in destinations.items():
                print(f"From {source} to {destination}:")
                for route in routes:
                    print(f" - {route['mode']} | Cost: {route['cost']} | Duration: {route['duration']} mins")

    def get_user_input(self):
        """Get validated user input for source and destination."""
        print("Available Sources:")
        print(", ".join(self.sources))
        print("\nAvailable Destinations:")
        print(", ".join(self.destinations))

        # Get source and destination with error handling
        while True:
            source = input("\nEnter the source: ")
            if source in self.sources:
                break
            else:
                print(f"[ERROR] '{source}' is not a valid source. Please choose from the available options.")
        
        while True:
            destination = input("Enter the destination: ")
            if destination in self.destinations:
                break
            else:
                print(f"[ERROR] '{destination}' is not a valid destination. Please choose from the available options.")
        
        return source, destination


# Usage
route_finder = RouteFinder()
route_finder.fetch_data()

# Get valid source and destination from the user
source, destination = route_finder.get_user_input()

# Fetch and print available routes
routes = route_finder.get_routes(source, destination)

if routes:
    print(f"\nAvailable routes from {source} to {destination}:")
    for route in routes:
        print(f" - {route['mode']} | Cost: {route['cost']} | Duration: {route['duration']} mins")
else:
    print(f"\nNo available routes found from {source} to {destination}.")
