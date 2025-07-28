
import os
import sys

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

#MAKE IT CUTE
def show_banner():
    print(r"""                                                                                   
                           █           
                         █████         
                        ███████        
                       █████████       
                      ███████████      
                     ██         ██     
                    █████      █████   
                   ███████    ███████  
                  █████████  █████████ 
                 ██████████████████████
 ______ ____ ______ ___   ___    ____ ____   ___   _____ ____
/_  __// __//_  __// _ \ / _ |  / __// __ \ / _ \ / ___// __/
 / /  / _/   / /  / , _// __ | / _/ / /_/ // , _// /__ / _/  
/_/  /___/  /_/  /_/|_|/_/ |_|/_/   \____//_/|_| \___//___/ 
    -----------sight - know - tell - conect------------                                          
""")

def show_menu():
    print("Select Module: ")
    print(r"""
        """)
    print("1. to run Skynet 777")
    print("2. to run Snitch")
    print("3. to run Veritas")
    print("4. to run Meister")
    print("Press Q to quit")
    print(r"""
        """)

def main():
    clear_console()
    show_banner()
    
    while True:
        show_menu()
        choice = input("Select an option: ").strip().lower()

        if choice == "1":
            import subprocess
            subprocess.run(["python", "modules/skynet_777.py"])

        if choice == "2":
            import subprocess
            subprocess.run(["python", "modules/snitch.py"])

        if choice == "3":
            import subprocess
            subprocess.run(["python", "modules/veritas.py"])

        if choice == "4":
            import subprocess
            subprocess.run(["python", "modules/meister.py"])

        if choice == "q":
            sys.exit()
        else:
            print("Choose one of the avaible options")
if __name__ == "__main__":
    main()