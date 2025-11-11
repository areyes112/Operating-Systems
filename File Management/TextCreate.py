import os
from faker import Faker

fake = Faker()

# Get Documents folder path (cross-platform)
documents_dir = os.path.join(os.path.expanduser("~"), "Documents")
os.makedirs(documents_dir, exist_ok=True)

file_path = os.path.join(documents_dir, "people.txt")

# --- Create and write 100 records ---
with open(file_path, mode='w', encoding='utf-8') as file:
    for _ in range(100):
        record = [
            fake.first_name(),
            fake.last_name(),
            fake.date_of_birth(minimum_age=18, maximum_age=90).strftime("%Y-%m-%d"),
            fake.numerify('##########'),
            fake.street_address(),
            fake.city(),
            fake.state_abbr(),
            fake.zipcode()
        ]
        line = ",".join(record) + "\n"
        file.write(line)

print(f"Created {file_path} with 100 records.")
