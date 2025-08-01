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


def search_entries(data, header):
    clear_console()
    print("\nSearch by:")
    print("1. Name")
    print("2. Phase")

    option = input("Choose an option (1-2): ").strip()
    if option not in {"1", "2"}:
        print("Invalid option.")
        return None

    query = input("Enter your search term: ").strip().lower()
    results = filter_data(data, option, query)

    if not results:
        print("\nNo matches found.")
        input("Press Enter to continue...")
        return None

    clear_console()
    print(f"\nFound {len(results)} result(s):\n")
    print(f"{header[0]:<15} {header[1]:<15} {header[2]:<8} {header[3]:<8}")
    print("-" * 50)
    for row in results:
        print(f"{row[0]:<15} {row[1]:<15} {row[2]:<8} {row[3]:<8}")

    input("\nPress Enter to continue...")
    return results

def filter_data(data, option, query):
    if option == "1":
        return [row for row in data if query in row[0].lower()]
    elif option == "2":
        return [row for row in data if row[2] == query]
    else:
        return []

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
    full_data = rows[1:]
    current_data = full_data 

    while True:
        clear_console()
        print("\n=== ENTRIES ===\n")
        print(f"{'No.':<5} {header[0]:<15} {header[1]:<15} {header[2]:<8} {header[3]:<8}")
        print("-" * 50)
        for i, row in enumerate(current_data, start=1):
            print(f"{i:<5} {row[0]:<15} {row[1]:<15} {row[2]:<8} {row[3]:<8}\n")

        choice = input(
            "Press 'f' to search, \n"
            "Press 'x' to sort, \n"
            "Press 'd' to open an entry, \n"
            "or 'b' to go back to the main menu: "
        ).strip().lower()

        if choice == "b": 
            break

        elif choice == "f":
            filtered = search_entries(current_data, header)
            if filtered is not None:
                current_data = filtered

        elif choice == "x": # DONE - TEST
            current_data = sort_entries(current_data)       

        elif choice == "d":
            if not current_data:
                print("\nNo entries to open.")
                input("Press Enter to continue...")
                continue

            selection = input("\nSelect a number to open (or 'c' to cancel): ").strip()
            if selection.lower() == 'c':
                print("Cancelled.")
                continue        

            try:
                index = int(selection) - 1
                if 0 <= index < len(current_data):
                    entry = current_data[index]
                    name, last_name, phase, grade = [x.strip() for x in entry[:4]]
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
                    print("Invalid selection.")
                    input("Press Enter to continue...")
            except ValueError:
                print("Invalid input.")
                input("Press Enter to continue...")

def show_menu():
    print("\nSelect an option:")
    print("1. Read Bio")
    print("Q. Quit")

def main():

    while True:
        clear_console()
        show_banner()
        show_menu()
        choice = input("Select an option: ").strip().lower()
        if choice == "1":
            read_bio()
        elif choice == "q":
            return
        else:
            print("Choose wisely")

if __name__ == "__main__":
    main()