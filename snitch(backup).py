import os
import csv
import subprocess

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_banner():
    print(r"""
           _               
      |\ |( ) |   __ |     
   __ | \| | _|_ /  \|__   
  /__ |  | |  | |    |  \  
   __/|  | |  |  \__/|  |  
          (_) |_           
        saw nothing      
      """)

#BIO READER
def read_bio():
    clear_console()
    try:
        with open("data/data.csv", "r") as file:
            rows = list(csv.reader(file))
    except FileNotFoundError:
        print("\nNo student data available.\n")
        return

    if len(rows) <= 1:
        print("\nNo student data available.\n")
        return

    header = rows[0]
    data = rows[1:]

    while True:
        clear_console()
        print("\n=== ENTRIES ===\n")
        print(f"{'No.':<5} {header[0]:<15} {header[1]:<15} {header[2]:<8} {header[3]:<8}")
        print("-" * 55)
        for i, row in enumerate(data, start=1):
            print(f"{i:<5} {row[0]:<15} {row[1]:<15} {row[2]:<8} {row[3]:<8}")

        choice = input("Select a number to open, Press 'x' to sort, Press 'z' to search or 'b' to go back to the main menu: ").strip().lower()

        if choice == "b":
            main()
            break
        elif choice == "x":
            data = sort_entries(data)
        elif choice == "z":
            # Placeholder for search functionality
            print("Search functionality is not implemented yet.")
            input("Press Enter to continue...")
        elif choice.isdigit():
            index = int(choice) - 1
            if index < 0 or index >= len(data):
                print("Invalid selection.")
                input("Press Enter to continue...")
                continue
            to_look = data[index]
            name, last_name, phase, grade = to_look[:4]
            filename = f"{name}_{last_name}_{phase}_{grade}_entry.txt"
            filepath = os.path.join("entries", filename)

            if os.path.exists(filepath):
                clear_console()
                print(f"\nReading: {filename}\n")
                print("=" * 50)
                with open(filepath, "r") as f:
                    print(f.read())
                print("=" * 50)
                input("\nPress Enter to return...")
            else:
                print(f"\nBio file not found: {filename}")
                input("Press Enter to continue...")
        else:
            print("Invalid input.")
            input("Press Enter to continue...")
#SORTING
def sort_entries(data):
    sort_options = {
        "1": ("Name (A-Z)", lambda x: x[0].lower()),
        "2": ("Last Name (A-Z)", lambda x: x[1].lower()),
        "3": ("Phase (ascending)", lambda x: int(x[2])),
        "4": ("Grade (ascending)", lambda x: int(x[3])),
        "5": ("No Sorting", None)
    }

    while True:
        clear_console()
        print("\nHow would you like to sort the results?")
        for key, (desc, _) in sort_options.items():
            print(f"{key}. {desc}")

        option = input("Choose an option (1-5): ").strip()
        if option in sort_options:
            sort_key = sort_options[option][1]
            if sort_key:
                data = sorted(data, key=sort_key)
            break
        else:
            print("Invalid option. Please choose again.")
    return data

def show_menu():
    print("\nSelect an option:")
    print("1. Read Bio")
    print("Q. Quit")

def main():
    clear_console()
    show_banner()
    while True:
        show_menu()
        choice = input("Select an option: ").strip().lower()
        if choice == "1":
            read_bio()
        elif choice == "q":
            print("Goodbye!")
            subprocess.run(["python", "tetraforce.py"])
            break
        else:
            print("Choose wisely")

main()
