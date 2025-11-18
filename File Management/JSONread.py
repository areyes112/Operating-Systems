import os
import json

# Cross-platform Documents path
documents_dir = os.path.join(os.path.expanduser("~"), "Documents")
file_path = os.path.join(documents_dir, "people.json")

# --- Read and print data ---
if not os.path.exists(file_path):
    print("File not found. Run create_json.py first.")
else:
    with open(file_path, mode='r', encoding='utf-8') as file:
        data = json.load(file)

    print(f"\n Loaded {len(data)} records from: {file_path}\n")
    header = ["First Name", "Last Name", "Date of Birth", "Phone", "Street", "City", "State", "Zip"]
    print("{:<12} {:<12} {:<16} {:<15} {:<35} {:<18} {:<6} {:<8}".format(*header))
    print("-" * 110)

    for person in data[:150]:
        print("{:<12} {:<12} {:<16} {:<15} {:<35} {:<18} {:<6} {:<8}".format(
            person["first_name"],
            person["last_name"],
            person["date_of_birth"],
            person["phone"],
            person["street"],
            person["city"],
            person["state"],
            person["zip"]
        ))

file_to_delete = "people.json"
file_path_to_delete = os.path.join(documents_dir, file_to_delete)
print(f"Checking for: {file_path_to_delete}")  # <-- Add this

if os.path.exists(file_path_to_delete):
    os.remove(file_path_to_delete)
    print(f"\nDeleted file: {file_path_to_delete}")
else:
    print("File not found — could not delete.")
