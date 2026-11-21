
from tracker import create_record
from datetime import datetime
import json

records = [
    create_record("Paris", "Visited Eiffel Tower", "15-05-2023"),
    create_record("London", "Explored Big Ben", "05-06-2022"),
    create_record("Dubai", "Enjoyed desert safari", "10-01-2024")
]

for record in records:
    date_object = datetime.strptime(record["visit_date"], "%d-%m-%Y")
    record["visit_date"] = date_object.strftime("%B %d, %Y")

json_data = json.dumps(records, indent=4)
print(json_data)

python_data = json.loads(json_data)

for record in python_data:
    print(record)
