import os

# Same cross-platform Documents path
documents_dir = os.path.join(os.path.expanduser("~"), "Documents")
file_path = os.path.join(documents_dir, "people.txt")

# --- Read and print data ---
if not os.path.exists(file_path):
    print("File not found. Run create_file.py first.")
else:
    with open(file_path, mode='r', encoding='utf-8') as file:
        lines = file.readlines()

    # Parse comma-delimited text into a list of lists
    data = [line.strip().split(",") for line in lines]

    print(f"\n📄 Loaded {len(data)} records from: {file_path}\n")
    header = ["First Name", "Last Name", "Date of Birth", "Phone", "Street", "City", "State", "Zip"]
    print("{:<12} {:<12} {:<12} {:<18} {:<25} {:<15} {:<6} {:<8}".format(*header))
    print("-" * 110)
    for row in data[:150]:  
        print("{:<12} {:<12} {:<12} {:<18} {:<25} {:<15} {:<6} {:<8}".format(*row))

file_to_delete = "people.txt"
file_path_to_delete = os.path.join(documents_dir, file_to_delete)
if os.path.exists(file_path_to_delete):
    os.remove(file_path_to_delete)
    print(f"\n🗑️  Deleted file: {file_path_to_delete}")