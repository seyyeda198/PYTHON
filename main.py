from tripdata import get_trip
from datetime import datetime
import json

trips = [
    get_trip("Paris", "15-05-2023", "Visited Eiffel Tower"),
    get_trip("London", "20-06-2023", "Explored Big Ben"),
    get_trip("Dubai", "10-01-2024", "Enjoyed desert safari")
]

for trip in trips:
    date_object = datetime.strptime(trip["date"], "%d-%m-%Y")
    trip["date"] = date_object.strftime("%B %d, %Y")

json_data = json.dumps(trips, indent=4)

print(json_data)
