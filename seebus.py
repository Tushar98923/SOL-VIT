from pymongo import MongoClient
from datetime import datetime


class RouteFinder:
    def __init__(self):
        """Initialize an empty graph."""
        self.graph = {}

    def add_route(self, source, destination, mode, cost, duration):
        """Add a route between source and destination with mode, cost, and duration."""
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
            try:
                source = flight.get("from")
                destination = flight.get("to")
                duration_minutes = self.convert_duration_to_minutes(flight.get("duration", "0h 0m"))
                cost = flight.get("price", 0)

                if source and destination:
                    self.add_route(source, destination, "flight", cost, duration_minutes)
                else:
                    print(f"[INFO] No valid route available for flight: {flight}")
            except Exception as e:
                print(f"[ERROR] Failed to process flight data: {e}")

        # === Map and add bus data ===
        for bus in bus_data:
            try:
                source = bus.get("source")
                destination = bus.get("destination")
                duration_minutes = self.calculate_duration(bus.get("departure"), bus.get("arrival"))
                cost = 300  # Default cost as no fare is available

                if source and destination:
                    self.add_route(source, destination, "bus", cost, duration_minutes)
                else:
                    print(f"[INFO] No valid route available for bus: {bus}")
            except Exception as e:
                print(f"[ERROR] Failed to process bus data: {e}")

        # === Map and add train data ===
        for train in train_data:
            try:
                source = train.get("source")
                destination = train.get("destination")
                duration_minutes = self.calculate_duration(train.get("departure_time"), train.get("arrival_time"))
                min_fare = min(train.get("fare", {}).values(), default=0)  # Get the lowest fare

                if source and destination:
                    self.add_route(source, destination, "train", min_fare, duration_minutes)
                else:
                    print(f"[INFO] No valid route available for train: {train}")
            except Exception as e:
                print(f"[ERROR] Failed to process train data: {e}")

        # === Map and add cab data ===
        for cab in cab_data:
            try:
                source = cab.get("from")
                destination = cab.get("to")
                cost = cab.get("fare", 0)
                duration = 45  # Default cab duration

                if source and destination:
                    self.add_route(source, destination, "cab", cost, duration)
                else:
                    print(f"[INFO] No valid route available for cab: {cab}")
            except Exception as e:
                print(f"[ERROR] Failed to process cab data: {e}")

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
        try:
            if isinstance(departure, str) and isinstance(arrival, str):
                dep_time = datetime.strptime(departure, "%H:%M")
                arr_time = datetime.strptime(arrival, "%H:%M")
                return int((arr_time - dep_time).seconds / 60)
            elif isinstance(departure, datetime) and isinstance(arrival, datetime):
                return int((arrival - departure).seconds / 60)
        except Exception as e:
            print(f"[ERROR] Failed to calculate duration: {e}")
        return 0

    def print_graph(self):
        """Print the populated graph to verify correctness."""
        if not self.graph:
            print("[INFO] No routes available.")
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
