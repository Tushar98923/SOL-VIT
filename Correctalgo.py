import random
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
            source = flight.get("from")
            destination = flight.get("to")
            duration_minutes = self.convert_duration_to_minutes(flight.get("duration", "0h 0m"))
            cost = flight.get("price", 0)

            if source and destination:
                self.add_route(source, destination, "flight", cost, duration_minutes)

        # === Map and add bus data ===
        for bus in bus_data:
            source = bus.get("source")
            destination = bus.get("destination")
            duration_minutes = self.calculate_duration(bus.get("departure"), bus.get("arrival"))
            cost = 300  # Default cost

            if source and destination:
                self.add_route(source, destination, "bus", cost, duration_minutes)

        # === Map and add train data ===
        for train in train_data:
            source = train.get("source")
            destination = train.get("destination")
            duration_minutes = self.calculate_duration(train.get("departure_time"), train.get("arrival_time"))
            min_fare = min(train.get("fare", {}).values(), default=0)  # Lowest fare

            if source and destination:
                self.add_route(source, destination, "train", min_fare, duration_minutes)

        # === Map and add cab data ===
        for cab in cab_data:
            source = cab.get("from")
            destination = cab.get("to")
            cost = cab.get("fare", 0)
            duration = 45  # Default cab duration

            if source and destination:
                self.add_route(source, destination, "cab", cost, duration)

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
        except Exception:
            return 0

    def get_random_routes(self, limit=5):
        """Generate 5 diverse and valid route suggestions."""
        possible_routes = []
        all_sources = list(self.graph.keys())
        visited_pairs = set()  # Track visited source-destination pairs

        # Try random combinations of sources and destinations
        for _ in range(50):  # Try multiple combinations to get valid routes
            source = random.choice(all_sources)
            if source not in self.graph:
                continue

            destinations = list(self.graph[source].keys())
            if not destinations:
                continue

            destination = random.choice(destinations)

            # Check if reverse route exists (avoid round trip)
            if (destination, source) in visited_pairs:
                continue

            routes = self.find_routes(source, destination)
            if routes:
                for route in routes:
                    route_tuple = tuple([(leg["source"], leg["destination"]) for leg in route])
                    if route_tuple not in visited_pairs:
                        possible_routes.append(route)
                        visited_pairs.add(route_tuple)

            # Stop if we have enough valid options
            if len(possible_routes) >= limit:
                break

        # Select 5 unique random routes
        if len(possible_routes) > limit:
            possible_routes = random.sample(possible_routes, limit)

        return possible_routes
    
    

    def find_routes(self, source, destination):
        """Find possible routes between source and destination, including connecting routes."""
        possible_routes = []

        # === Check Direct Route ===
        if source in self.graph and destination in self.graph[source]:
            for route in self.graph[source][destination]:
                possible_routes.append([{
                    "mode": route["mode"],
                    "source": source,
                    "destination": destination,
                    "cost": route["cost"],
                    "duration": route["duration"]
                }])

        # === Check 1-hop Connection (source → stop → destination) ===
        if source in self.graph:
            for stop in self.graph[source]:
                if stop in self.graph and destination in self.graph[stop]:
                    for route1 in self.graph[source][stop]:
                        for route2 in self.graph[stop][destination]:
                            possible_routes.append([
                                {
                                    "mode": route1["mode"],
                                    "source": source,
                                    "destination": stop,
                                    "cost": route1["cost"],
                                    "duration": route1["duration"]
                                },
                                {
                                    "mode": route2["mode"],
                                    "source": stop,
                                    "destination": destination,
                                    "cost": route2["cost"],
                                    "duration": route2["duration"]
                                }
                            ])

        return possible_routes

    def print_route_summaries(self, possible_routes):
        """Print only the start and end points for route selection."""
        if not possible_routes:
            print("[INFO] No valid routes available.")
            return

        print("\n--- Available Routes ---")
        for idx, route_set in enumerate(possible_routes, start=1):
            start = route_set[0]["source"]
            end = route_set[-1]["destination"]
            print(f"{idx}. {start} → {end}")

    def print_full_route_details(self, selected_route):
        """Print detailed information about the selected route."""
        if not selected_route:
            print("[ERROR] No route selected or route is invalid.")
            return

        total_cost, total_duration = 0, 0
        print("\n--- Selected Route Details ---")
        for route in selected_route:
            print(f"{route['mode'].capitalize()} from {route['source']} to {route['destination']} | "
                  f"Cost: {route['cost']}, Duration: {route['duration']} mins")
            total_cost += route["cost"]
            total_duration += route["duration"]

        print(f"\nTotal Cost: {total_cost}, Total Duration: {total_duration} mins")


# === RUN TEST ===
route_finder = RouteFinder()
route_finder.fetch_data_and_populate_graph()

# Generate 5 random possible routes and display summaries
possible_routes = route_finder.get_random_routes(limit=5)
route_finder.print_route_summaries(possible_routes)

# Ask user to choose a route
try:
    choice = int(input("\nEnter the number of the route you want to select (1-5): "))
    if 1 <= choice <= len(possible_routes):
        selected_route = possible_routes[choice - 1]
        route_finder.print_full_route_details(selected_route)
    else:
        print("[ERROR] Invalid selection. Please choose a number between 1 and 5.")
except ValueError:
    print("[ERROR] Invalid input. Please enter a number.")
