import os
import csv

def clear_console():
 os.system('cls' if os.name == 'nt' else 'clear')

def show_banner():
    print(r""" 
|               
  __ `__ \    _ \  |   __|  __|   _ \   __| 
  |   |   |   __/  | \__ \  |     __/  |    
 _|  _|  _| \___| _| ____/ \__| \___| _|  
     ---\\\\execute order 66////---
          """)

def add_class():
    clear_console()
    class_name = input("Enter the name of the class to add: ").strip()
    if not class_name:
        print("Class name cannot be empty.")
        return
    
    classes_dir = "data/meister_data/classes"
    os.makedirs(classes_dir, exist_ok=True)

    filename = os.path.join(classes_dir, f"{class_name}.csv")
    if os.path.exists(filename):
        print(f"Class '{class_name}' already exists.")
        return

    with open(filename, "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Name", "Last Name"])  

    print(f"Class '{class_name}' created at {filename}.")

def list_classes():
     if not os.path.exists("data/meister_data/classes"):
        print("\nNo classes found.\n")
        return
     
    # List all classes in the directory
    # Allow user to select a class to view or edit
    # Allow user to delete a class
    # Allow user to add students to a class

def manage_classes():
    clear_console()
    print("Manage Classes:")
    print("1. Add Class")
    print("2. List Classes")
    print("Press Q to quit")

    choice = input("Select an option: ").strip().lower()
    if choice == "1":
        add_class()
    elif choice == "2":
        list_classes()
    elif choice == "q":
        return


def show_menu():
    print("Select an option: ")
    print(r""" 
        """)
    print("1. Registry")
    print("2. Manage Classes")
    print("3. Tools")
    print("Press Q to quit")

def main():    
        clear_console()
        show_banner()

        while True:
                show_menu()
                choice = input("Select and option: ")

                if choice == "1":
                        pass
                elif choice == "2":
                        manage_classes()
                if choice == "q":
                        return


if __name__ == "__main__":
    main()