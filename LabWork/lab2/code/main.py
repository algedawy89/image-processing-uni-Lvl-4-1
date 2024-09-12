import subprocess as sp
from colorama import init, Fore, Style



while True:
    try:
        print(Fore.GREEN+"====================")
        print(Fore.YELLOW+"Choose an option:"+Style.RESET_ALL)
        print(Fore.BLUE+"1. Cropping \n2. Resize \n3. Rotation \n4. Last"+Style.RESET_ALL)
        print(Fore.GREEN+"===================="+Style.RESET_ALL)
        x = int(input(Fore.GREEN+"Choose: "+Style.RESET_ALL))
        
        if x == 1:
            sp.run("python croping.py", shell=True)
        elif x == 2:
            sp.run("python resize.py", shell=True)
        elif x == 3:
            sp.run("python Rotation_Tr.py", shell=True)
        elif x == 4:
            sp.run("python last.py", shell=True)
        else:
            print(Fore.RED+"Invalid choice, please try again"+ Style.RESET_ALL)
            
    except ValueError:
          print(Fore.YELLOW + "Error: Please enter a numeric value." + Style.RESET_ALL)
