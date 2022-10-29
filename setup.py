import os
import sys
from pathlib import Path
INSTALL_DIR = '/usr/bin/'
path_to_file = '/usr/bin/BxPP'
path = Path(path_to_file)
if path.is_file():
    print('want to reinstall?')
    while True:
        option = input("(y/n)")
        if option =='y':
            os.system('clear')
            print("Reinstalling!")
            os.system("sudo rm -r /usr/bin/BxPP/")
            print("Finished!")
            break
        else:
            sys.exit('no update your you :p')
os.system(f'sudo git clone https://github.com/Discordmodsbers/BxPP {INSTALL_DIR}')
os.system('echo alias BxPP="python3 /usr/bin/BxPP/BxPP.py" >> ~/.bashrc ')
os.system('sudo source ')
os.system('sudo apt update -y')
os.system('sudo apt-get upgrade -y')

os.system('clear')
print("Now all you have to run my interpeter is typing 'BxPP' with a file ofc.")
 
