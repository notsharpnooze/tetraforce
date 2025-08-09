import os

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

#MAIN FUNCTIONS




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
                if choice == "q":
                        return

                else:
                    print("Choose wisely")

if __name__ == "__main__":
    main()