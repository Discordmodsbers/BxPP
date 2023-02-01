import os
import time 

delay = 2

def cls():
  os.system('clear')

def deleter():
  try:
    for delete in range(10):
      print(f'Deleting {delete}%', end='\r')
      time.sleep(0.5)
    os.system("rm BxPP.py")
    os.system("rm CurrentVersion.py")
    os.system("rm grammar.txt")
    os.system("rm shell.py")
    os.syste('rm strings_wtih_arrows.py')
    return True
  except:
    print("Failed to update please run as sudo !")
    return False
    sys.exit()


def downloader():
  try:
    for download in range(11, 21):
      print(f"Downloading {download}%", end='\r')
      time.sleep(0.5)
    os.system('curl -LJO https://raw.githubusercontent.com/Discordmodsbers/BxPP/main/BxPP.py')
    os.system('curl -LJO https://raw.githubusercontent.com/Discordmodsbers/BxPP/main/Current_Version.py')
    os.system('curl -LJO https://raw.githubusercontent.com/Discordmodsbers/BxPP/main/grammar.txt')
    os.system('curl -LJO https://raw.githubusercontent.com/Discordmodsbers/BxPP/main/shell.py')
    os.system('curl -LJO https://raw.githubusercontent.com/Discordmodsbers/BxPP/main/strings_with_arrows.py')
    return True
  except:
    print("Failed to download !")
    return False
    sys.exit()


def main():
  cls()
  print("""""")
  print("[*] Deleting All Files [*]")
  if deleter():
    print("[*] Deleted All Files [*]")
    
  if downloader():
    print("[*] Downloaded everything ! [*]")


main()
