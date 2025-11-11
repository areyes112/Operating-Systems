# ====================================================
# File Handling Project
# Demonstrates file creation, writing, appending, and reading
# ====================================================

def create_and_write():
    """Program 1: Create and write data to a new file"""
    try:
        with open("students.txt", "w") as file:
            file.write("ID,Name,Grade\n")
            file.write("1,Alex,90\n")
            file.write("2,Bailey,85\n")
        print("\n✅ File 'students.txt' created and data written successfully.\n")
    except Exception as e:
        print(f"❌ Error creating file: {e}")


def append_data():
    """Program 2: Append data to an existing file"""
    try:
        with open("students.txt", "a") as file:
            file.write("3,Charlie,88\n")
            file.write("4,Dakota,92\n")
        print("\n✅ Data appended successfully to 'students.txt'.\n")
    except FileNotFoundError:
        print("\n⚠️ File not found. Please run option 1 first.\n")
    except Exception as e:
        print(f"❌ Error appending data: {e}")


def read_file():
    """Program 3: Read and display contents of a text file"""
    try:
        with open("students.txt", "r") as file:
            print("\n📖 File Contents (students.txt):\n")
            for line in file:
                print(line.strip())
            print()
    except FileNotFoundError:
        print("\n⚠️ File not found. Please create it first (Option 1).\n")
    except Exception as e:
        print(f"❌ Error reading file: {e}")


def write_structured():
    """Program 4: Create and write structured CSV-style data"""
    try:
        with open("sales.csv", "w") as file:
            file.write("Product,Quantity,Price\n")
            file.write("Laptop,3,1200\n")
            file.write("Mouse,10,25\n")
            file.write("Keyboard,5,45\n")
        print("\n✅ Structured data written to 'sales.csv'.\n")
    except Exception as e:
        print(f"❌ Error writing structured data: {e}")


def append_structured():
    """Program 5: Append new records to the CSV file"""
    try:
        with open("sales.csv", "a") as file:
            file.write("Monitor,2,300\n")
            file.write("Headphones,4,75\n")
        print("\n✅ Structured data appended to 'sales.csv'.\n")
    except FileNotFoundError:
        print("\n⚠️ 'sales.csv' not found. Please run option 4 first.\n")
    except Exception as e:
        print(f"❌ Error appending structured data: {e}")


def read_and_process():
    """Program 6: Read structured data and calculate total sales"""
    try:
        total_sales = 0
        with open("sales.csv", "r") as file:
            next(file)  # Skip header
            for line in file:
                product, quantity, price = line.strip().split(",")
                total_sales += int(quantity) * float(price)
        print(f"\n💰 Total Sales Amount: ${total_sales:.2f}\n")
    except FileNotFoundError:
        print("\n⚠️ 'sales.csv' not found. Please run option 4 first.\n")
    except Exception as e:
        print(f"❌ Error processing file: {e}")


# ====================================================
# Main Menu
# ====================================================

def main():
    while True:
        print("=====================================")
        print("   FILE HANDLING PROJECT MENU")
        print("=====================================")
        print("1. Create and write new student file")
        print("2. Append data to student file")

