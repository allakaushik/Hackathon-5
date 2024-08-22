import datetime

charging_stations = [
    {"id": 1, "name": "Station A", "location": "City Center", "slots": 5},
    {"id": 2, "name": "Station B", "location": "East Side", "slots": 3},
    {"id": 3, "name": "Station C", "location": "West End", "slots": 2},
    {"id": 4, "name": "Station D", "location": "North Park", "slots": 4},
]


def find_stations(location=None, min_slots=1):
    available_stations = []
    for station in charging_stations:
        if station["slots"] >= min_slots and (
            location is None or station["location"] == location
        ):
            available_stations.append(station)
    return available_stations


def book_slot(station_id):
    for station in charging_stations:
        if station["id"] == station_id:
            if station["slots"] > 0:
                station["slots"] -= 1
                print(
                    f"Slot booked at {station['name']}. Remaining slots: {station['slots']}"
                )
            else:
                print("No available slots at this station.")
            return
    print("Station not found.")


print("Welcome to the EV Charging Station Finder")

user_location = input("Enter the location you're interested in: ")
min_slots = int(input("Enter the minimum number of slots you need: "))

stations = find_stations(location=user_location, min_slots=min_slots)
if not stations:
    print(f"No stations available in {user_location} with at least {min_slots} slots.")
else:
    print(f"\nAvailable stations in {user_location} with at least {min_slots} slots:")
    for station in stations:
        print(
            f"ID: {station['id']}, Name: {station['name']}, Slots Available: {station['slots']}"
        )

    station_id = int(
        input("\nEnter the ID of the station you want to book a slot at: ")
    )
    book_slot(station_id=station_id)

print("\nRemaining stations after booking:")
for station in charging_stations:
    print(
        f"ID: {station['id']}, Name: {station['name']}, Slots Available: {station['slots']}"
    )
