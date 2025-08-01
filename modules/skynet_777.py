import csv
import os
import subprocess
#Keep it clean
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

#MAKE IT CUTE
def show_banner():
    print(r""" 
                                                                                           
 ███████  ██   ███ ███   ██  ████████   ███████ █████████      ███████  ████████  ████████ 
███       ██ ███    ██  ██   ██     ██  ██          ██              ██       ██        ██  
  ████    ████       ████    ██     ██  ███████     ██            ███       ███       ██   
     ███  ████        ███    ██     ██  ██          ██            ██        ██       ███   
      ███ ██  ██      ██     ██     ██  ██          ██           ██       ███        ██    
 ███████  ██   ███    ██     ██     ██  ███████     ██          ██        ██       ███     
                           ----- ...We watch over you... -----                                                                             
""")


def data_entry():
   
    def write_csv_header_if_needed(writer, file_exists): 
        header = ["Name", "Last Name", "Phase", "Grade", "Parent Name", "Parent Number", "Parent Mail"]
        if not file_exists or os.path.getsize("data/data.csv") == 0:
            writer.writerow(header)
    clear_console()

    print("\n=== DATA ENTRY ===\n")
    name = input("Enter student name: ").strip()            
    last_name = input("Enter student last name: ").strip()

    # Phases options
    valid_phases = {"5", "6", "7"}
    while True:
        phase = input("Enter student's phase (5, 6, 7): ").strip()
        if phase in valid_phases:
            break
        print("Enter: 5, 6 or 7.")

    # Per Phase
    valid_phases_grades = {
        "5": {"7", "8"},
        "6": {"9", "10"},
        "7": {"11", "12"}
    }
    valid_grades = valid_phases_grades[phase]
    print(f"Add a grade: {', '.join(valid_grades)}")

    while True:
        grade = input("Enter student's grade: ").strip()
        if grade in valid_grades:
            break
        print(f"Pick a grade: {', '.join(valid_grades)}")

    parent_name = input("Parent's name: ").strip()
    parent_number = input("Parent's number: ").strip()
    parent_mail = input("Parent's mail: ").strip()

    # Writes on CSV file
    os.makedirs("data", exist_ok=True)
    file_exists = os.path.exists("data/data.csv")
    with open("data/data.csv", "a", newline="") as file:
        writer = csv.writer(file)
        # Write header only if file is empty
        write_csv_header_if_needed(writer, file_exists)
        writer.writerow([name, last_name, phase, grade, parent_name, parent_number, parent_mail])
    print(f"Entry for {name} {last_name} saved.")

    # Creates a BIO
    os.makedirs("entries", exist_ok=True)
    filename = f"{name}_{last_name}_{phase}_{grade}_entry.txt"
    filepath = os.path.join("entries", filename)

    # Sets the TXT template
    with open(filepath, "w") as f:
        f.write("=== STUDENT INFORMATION ===\n")
        f.write(f"First Name: {name}\n")
        f.write(f"Last Name:  {last_name}\n")
        f.write(f"Parent's Name:  {parent_name}\n")
        f.write(f"Parent's Number:  {parent_number}\n")
        f.write(f"Parent's Mail:  {parent_mail}\n")
        f.write("\n=== ACADEMIC DATA ===\n")
        f.write(f"Phase:      {phase}\n")
        f.write(f"Grade:      {grade}\n")

# Creates notes, progress and comments files
    os.makedirs("entries/notes", exist_ok=True)
    filename_notes = f"{name}_{last_name}_{phase}_{grade}_notes.txt"
    filepath_notes = os.path.join("entries/notes", filename_notes)
    
    with open(filepath_notes, "w") as f:
        f.write("\n=== NOTES ===\nNone\n")
    
    os.makedirs("entries/progress", exist_ok=True)
    filename_progress = f"{name}_{last_name}_{phase}_{grade}_progress.txt"
    filepath_progress = os.path.join("entries/progress", filename_progress)

    with open(filepath_progress, "w") as f:
        f.write("\n=== PROGRESS ===\nNone\n")

    os.makedirs("entries/comments", exist_ok=True)
    filename_comments = f"{name}_{last_name}_{phase}_{grade}_comments.txt"
    filepath_comments = os.path.join("entries/comments", filename_comments)

    with open(filepath_comments, "w") as f:
        f.write("\n=== COMMENTS ===\nNone\n")
#ENDS
    clear_console()
    print(f"\nEntry saved and file created at: entries/{filename}\n")
    input("Press Enter to continue...")

#END OF THE ENTRY LOOP
def end_of_data_entry():
    while True:
        data_entry()
        response = input("Do you have more entries? (y/n): ").strip().lower()
        while response not in {"y", "n"}:
            print("Answer with (y) or (n), (y) means yes, (n) means no")
            response = input("Do you have more entries? (y/n): ").strip().lower()
        if response == "n":
            print("Returning to main menu...")
            break

#SEARCH ENGINE ----- UPDATED

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

def view_all_entries():
    if not os.path.exists("data/data.csv"):
        print("\n No data found. Add some... \n")
        return
    
    with open("data/data.csv", "r") as file:
        rows = list(csv.reader(file))

    if len(rows) <= 1:
        print("\n The file is empty or has only headers. \n")
        return
    
    header = rows[0]
    full_data = rows[1:]
    current_data = full_data 

    while True:
            clear_console()
            print("\nSTUDENT ENTRIES:\n")
            print(f"{'No.':<5}{header[0]:<15} {header[1]:<15} {header[2]:<8} {header[3]:<8}")
            print("-" * 50)
            for i, row in enumerate(current_data, start=1):
                print(f"{i:<5} {row[0]:<15} {row[1]:<15} {row[2]:<8} {row[3]:<8}")
            print()

            choice = input(
                "Press 'f' to search, \n"
                "Press 'x' to sort, \n"
                "Press 'd' to delete an entry, \n"
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
                    print("\nNo entries to delete.")
                    input("Press Enter to continue...")
                    continue

                selection = input("\nSelect a number to delete (or 'c' to cancel): ").strip()
                if selection.lower() == 'c':
                    print("Cancelled.")
                    continue

                try:
                    index = int(selection) - 1
                    if index < 0 or index >= len(current_data):
                        print("Invalid selection.")
                        input("Press Enter to continue...")
                        continue
                    to_delete = current_data[index]
                except ValueError:
                    print("Invalid input.")
                    input("Press Enter to continue...")
                    continue

                print(f"\nAre you sure you want to delete {to_delete[0]} {to_delete[1]} (Phase {to_delete[2]}, Grade {to_delete[3]})?")
                confirm = input("Type 'y' to confirm: ").strip().lower()
                if confirm != "y":
                    print("Delete cancelled.")
                    input("Press Enter to continue...")
                    continue

                # Remove from current_data and full_data
                current_data.pop(index)
                try:
                    full_data.remove(to_delete)
                except ValueError:
                    pass  # If filtered, may not be in full_data

                # Rewrite CSV
                with open("data/data.csv", "w", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow(header)
                    writer.writerows(full_data)

                # Delete TXT file
                filename = f"{to_delete[0]}_{to_delete[1]}_{to_delete[2]}_{to_delete[3]}_entry.txt"
                filepath = os.path.join("entries", filename)
                if os.path.exists(filepath):
                    os.remove(filepath)
                    print(f"\nFile deleted: entries/{filename}")
                else:
                    print(f"\nTXT file not found: {filename}")

                print("Entry successfully deleted.\n")
                input("Press Enter to continue...")                
            
            
            else:
                print("Invalid option.")

#MENU AND ITS PARTS
def show_menu():
    clear_console()
    show_banner()

    print("\nMAIN MENU")
    print("1. Data Entry")
    print("2. View All Entries")
    print("3. Credits")
    print("Q. Exit")
    print("Program Version 0.2 - You are terminated...")

#JUST IN CASE
def show_credits():
    print(r"""
          "Made by Not_Sharpnooze, using Python.
                wish me lunch... "
          """)

# === MAIN MENU SETTINGS ===
def main():
    try:
        while True:
            show_menu()
            choice = input("Select an option: ").strip().lower()

            if choice == "1":
                data_entry()
            elif choice == "2":
                view_all_entries()
            elif choice == "3":
                show_credits()
            elif choice == "q":
                print("Hasta la vista...")
                return
            else:
                print("Choose wisely")
    except KeyboardInterrupt:
        print("\nExiting program. Goodbye!")

if __name__ == "__main__":
    main()