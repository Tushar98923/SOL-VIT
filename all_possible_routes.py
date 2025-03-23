from pymongo import MongoClient
from datetime import datetime, timedelta


class RouteFinder:
    def __init__(self):
        """Initialize an empty graph."""
        self.graph = {}

    def add_route(self, source, destination, mode, cost, duration):
        """Add a route between source and destination with mode, cost, and duration."""
        # Skip if source or destination is None
        if not source or not destination:
            print(f"[WARNING] Skipping invalid route: {source} -> {destination}")
            return

        if source not in self.graph:
            self.graph[source] = {}
        if destination not in self.graph[source]:
            self.graph[source][destination] = []
        self.graph[source][destination].append({
            "mode": mode,
            "cost": cost,
            "duration": duration
        })

    def fetch_data_and_populate_graph(self):
        """Fetch data from MongoDB and add it to the graph."""
        client = MongoClient('mongodb://localhost:27017/')
        db = client["travel_app"]

        # === Fetch data from all collections ===
        flight_data = list(db["flights"].find())
        bus_data = list(db["buses"].find())
        train_data = list(db["trains"].find())
        cab_data = list(db["cabs"].find())

        # === Map and add flight data ===
        for flight in flight_data:
            duration_minutes = self.convert_duration_to_minutes(flight.get("duration", "0h 0m"))
            self.add_route(
                flight.get("from", None),
                flight.get("to", None),
                "flight",
                flight.get("price", 0),
                duration_minutes
            )

        # === Map and add bus data ===
        for bus in bus_data:
            duration_minutes = self.calculate_duration(bus.get("departure"), bus.get("arrival"))
            self.add_route(
                bus.get("source", None),
                bus.get("destination", None),
                "bus",
                300,  # Default cost as no fare is available
                duration_minutes
            )

        # === Map and add train data ===
        for train in train_data:
            duration_minutes = self.calculate_duration(train.get("departure_time"), train.get("arrival_time"))
            min_fare = min(train.get("fare", {}).values(), default=0)  # Get the lowest fare
            self.add_route(
                train.get("source", None),
                train.get("destination", None),
                "train",
                min_fare,
                duration_minutes
            )

        # === Map and add cab data ===
        for cab in cab_data:
            self.add_route(
                cab.get("from", None),  # Correct field name
                cab.get("to", None),    # Correct field name
                "cab",
                cab.get("fare", 0),     # Correct field name for fare
                45  # Default cab duration (can be adjusted based on distance later)
            )

        # Print confirmation after graph is populated
        print("[INFO] Graph populated successfully.")

    def convert_duration_to_minutes(self, duration_str):
        """Convert flight duration string (e.g., '2h 30m') to minutes."""
        if not duration_str:
            return 0
        hours, minutes = 0, 0
        parts = duration_str.split()
        for part in parts:
            if "h" in part:
                hours = int(part.replace("h", ""))
            elif "m" in part:
                minutes = int(part.replace("m", ""))
        return hours * 60 + minutes

    def calculate_duration(self, departure, arrival):
        """Calculate duration in minutes from departure and arrival time."""
        if isinstance(departure, str) and isinstance(arrival, str):
            # Convert string time for bus to datetime object
            try:
                dep_time = datetime.strptime(departure, "%H:%M")
                arr_time = datetime.strptime(arrival, "%H:%M")
                duration = (arr_time - dep_time).seconds / 60
                return int(duration)
            except ValueError:
                return 0
        elif isinstance(departure, datetime) and isinstance(arrival, datetime):
            # Calculate duration for trains with datetime
            duration = (arrival - departure).seconds / 60
            return int(duration)
        return 0

    def print_graph(self):
        """Print the populated graph to verify correctness."""
        if not self.graph:
            print("[WARNING] Graph is still empty!")
            return

        for source, destinations in self.graph.items():
            for destination, routes in destinations.items():
                print(f"From {source} to {destination}:")
                for route in routes:
                    print(f" - Mode: {route['mode']}, Cost: {route['cost']}, Duration: {route['duration']} mins")


# === RUN TEST ===
route_finder = RouteFinder()
route_finder.fetch_data_and_populate_graph()
route_finder.print_graph()
