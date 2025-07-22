import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_banner():
 print("""
 _          _       _            _            _        _            _                  _        
/\ \    _ / /\     /\ \         /\ \         /\ \     /\ \         / /\               / /\      
\ \ \  /_/ / /    /  \ \       /  \ \        \ \ \    \_\ \       / /  \             / /  \     
 \ \ \ \___\/    / /\ \ \     / /\ \ \       /\ \_\   /\__ \     / / /\ \           / / /\ \__  
 / / /  \ \ \   / / /\ \_\   / / /\ \_\     / /\/_/  / /_ \ \   / / /\ \ \         / / /\ \___\ 
 \ \ \   \_\ \ / /_/_ \/_/  / / /_/ / /    / / /    / / /\ \ \ / / /  \ \ \        \ \ \ \/___/ 
  \ \ \  / / // /____/\    / / /__\/ /    / / /    / / /  \/_// / /___/ /\ \        \ \ \       
   \ \ \/ / // /\____\/   / / /_____/    / / /    / / /      / / /_____/ /\ \   _    \ \ \      
    \ \ \/ // / /______  / / /\ \ \  ___/ / /__  / / /      / /_________/\ \ \ /_/\__/ / /      
     \ \  // / /_______\/ / /  \ \ \/\__\/_/___\/_/ /      / / /_       __\ \_\\ \/___/ /       
      \_\/ \/__________/\/_/    \_\/\/_________/\_\/       \_\___\     /____/_/ \_____\/        
         "You shall know the truth, and the truth shall make you free" - John 8:32
 """)

def show_menu():
    print("Select an option: ")
    print(r""" 
        """)
    print("1.")
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
                        import subprocess
                        subprocess.run(["python", "tetraforce.py"])
                        break

        else:
                print("Choose wisely")
main()