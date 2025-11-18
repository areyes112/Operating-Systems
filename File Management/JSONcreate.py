import os
import json
from faker import Faker

fake = Faker()

# Cross-platform Documents directory
documents_dir = os.path.join(os.path.expanduser("~"), "Documents")
os.makedirs(documents_dir, exist_ok=True)

file_path = os.path.join(documents_dir, "people.json")

# --- Create and write 100 records ---
records = []
for _ in range(100):
    person = {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "date_of_birth": fake.date_of_birth(minimum_age=18, maximum_age=90).strftime("%Y-%m-%d"),
        "phone": fake.numerify('##########'),
        "street": fake.street_address(),
        "city": fake.city(),
        "state": fake.state_abbr(),
        "zip": fake.zipcode()
    }
    records.append(person)

# Write all records to the JSON file
with open(file_path, mode='w', encoding='utf-8') as file:
    json.dump(records, file, indent=4)

print(f"Created {file_path} with 100 records.")
