import os
from faker import Faker

fake = Faker()

# Same cross-platform Documents path
documents_dir = os.path.join(os.path.expanduser("~"), "Documents")
file_path = os.path.join(documents_dir, "people.txt")

# --- Append 50 more records ---
if not os.path.exists(file_path):
    print("File not found. Run create_file.py first.")
else:
    with open(file_path, mode='a', encoding='utf-8') as file:
        for _ in range(50):
            record = [
                fake.first_name(),
                fake.last_name(),
                fake.date_of_birth(minimum_age=18, maximum_age=90).strftime("%Y-%m-%d"),
                fake.phone_number(),
                fake.street_address(),
                fake.city(),
                fake.state_abbr(),
                fake.zipcode()
            ]
            line = ",".join(record) + "\n"
            file.write(line)

    print(f"Appended 50 records to {file_path}.")
