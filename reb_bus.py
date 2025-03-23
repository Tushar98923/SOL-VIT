from pymongo import MongoClient


def fetch_data():
    """Connect to MongoDB and fetch raw data from all collections."""
    try:
        client = MongoClient('mongodb://localhost:27017/')
        db = client["travel_app"]

        # Fetch all data from respective collections
        flight_data = list(db["flights"].find())
        bus_data = list(db["buses"].find())
        train_data = list(db["trains"].find())
        cab_data = list(db["cabs"].find())

        # Print raw data to verify connection and schema
        print("==== Flights ====")
        for flight in flight_data:
            print(flight)

        print("\n==== Buses ====")
        for bus in bus_data:
            print(bus)

        print("\n==== Trains ====")
        for train in train_data:
            print(train)

        print("\n==== Cabs ====")
        for cab in cab_data:
            print(cab)

    except Exception as e:
        print(f"[ERROR] Failed to fetch data: {e}")


# Run the test function
fetch_data()
