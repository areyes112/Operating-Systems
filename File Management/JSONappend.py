import os
import json
from faker import Faker

fake = Faker()

# Cross-platform Documents path
documents_dir = os.path.join(os.path.expanduser("~"), "Documents")
file_path = os.path.join(documents_dir, "people.json")

# --- Append 50 new records ---
if not os.path.exists(file_path):
    print("File not found. Run create_json.py first.")
else:
    with open(file_path, mode='r', encoding='utf-8') as file:
        records = json.load(file)

    for _ in range(50):
        person = {
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "date_of_birth": fake.date_of_birth(minimum_age=18, maximum_age=90).strftime("%Y-%m-%d"),
            "phone": fake.phone_number(),
            "street": fake.street_address(),
            "city": fake.city(),
            "state": fake.state_abbr(),
            "zip": fake.zipcode()
        }
        records.append(person)

    with open(file_path, mode='w', encoding='utf-8') as file:
        json.dump(records, file, indent=4)

    print(f"Appended 50 records to {file_path}. Total now: {len(records)}.")

