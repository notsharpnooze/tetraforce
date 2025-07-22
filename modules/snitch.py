import os
import csv

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
    with open("data/data.csv", "r") as file:
        rows = list(csv.reader(file))

    if len(rows) <= 1: #if its empty
        print("\n No student data available.\n")
        return
    
    header = rows[0] #Top of file
    data = rows[1:].copy()  #From 1 and on...

    while True:
        filtered = data
        os.system("cls" if os.name == "nt" else "clear")

        clear_console()
        print("\n=== ENTRIES ===\n")
        print(f"{'No.':<5} {header[0]:<15} {header[1]:<15} {header[2]:<8} {header[3]:<8}")
        print("-" * 55)
        for i, row in enumerate(filtered, start=1):
            print(f"{i:<5} {row[0]:<15} {row[1]:<15} {row[2]:<8} {row[3]:<8}")

        choice = input("Select a number to open, Press 'x' to sort, Press 'z' to search or 'b' to go back to the main menu: ").strip().lower()

        if choice == "b":
            main()  # or break if you're in a loop
        elif choice == "x":
            data = sort_entries(data)
        elif choice == "z":
            search(data, header)

        elif choice.isdigit():
            index = int(choice) - 1
            if index < 0 or index >= len(filtered):
                print("Invalid selection.")
                input("Press Enter to continue...")
                continue
            to_look = filtered[index]
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
                
def search(data, header):
    clear_console()
    print("\nHow would you like to search?")
    print("1. Name")
    print("2. Last Name")
    print("3. Phase")
    print("4. Show All")

    option = input("Choose an option (1-4): ").strip().lower()

    if option in {"1", "2", "3", "1"}:
        query = input("Enter your search term: ").strip().lower()

        if option == "1":
            filtered = [row for row in data if query in row[0].lower()]
        elif option == "2":
            filtered = [row for row in data if query in row[1].lower()]
        elif option == "3":
            filtered = [row for row in data if row[2] == query]
    elif option == "4":
        filtered = data
    else:
        print("Invalid option.")
        return

    if not filtered:
        print("\nNo matching entries found.")
        return

    filtered = sort_entries(filtered) 

    clear_console()
    print("\n=== ENTRIES ===\n")
    print(f"{'No.':<5} {header[0]:<15} {header[1]:<15} {header[2]:<8} {header[3]:<8}")
    print("-" * 55)
    for i, row in enumerate(filtered, start=1):
        print(f"{i:<5} {row[0]:<15} {row[1]:<15} {row[2]:<8} {row[3]:<8}")

    selection = input("\nSelect a number to open (or 'c' to cancel): ").strip()

    if selection.lower() == 'c':
        print("Cancelled.")
        return

    elif selection.isdigit():
                index = int(selection) - 1
                if index < 0 or index >= len(filtered):
                    print("Invalid selection.")
                    input("Press Enter to continue...")
                    
                to_look = filtered[index]
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

    clear_console()
    print("\nHow would you like to sort the results?")
    print("1. Name (A-Z)")
    print("2. Last Name (A-Z)")
    print("3. Phase (ascending)")
    print("4. Grade (ascending)")
    print("5. No Sorting")

    option = input("Choose an option (1-5): ").strip()

    if option == "1":
        data.sort(key=lambda x: x[0].lower())  # First Name
    elif option == "2":
        data.sort(key=lambda x: x[1].lower())  # Last Name
    elif option == "3":
        data.sort(key=lambda x: int(x[2]))     # Phase
    elif option == "4":
        data.sort(key=lambda x: int(x[3]))     # Grade
    elif option == "5":
        pass  # No sorting
    else:
        print("Invalid option. Showing unsorted data.")
    return data

def show_menu():
    print("Select an option: ")
    print()
    print("1.Read Bio")
    print("Press Q to quit")

def main():    
    clear_console()
    show_banner()

    while True:
        show_menu()
        choice = input("Select and option: ")

        if choice == "1":
            read_bio()
        if choice == "q":
            import subprocess
            subprocess.run(["python", "tetraforce.py"])
            break

        else:
            print("Choose wisely")
main()
