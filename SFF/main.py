import os, platform
from colorama import init, Fore
init()
os.system("title Soul Files Finder")
os.system('cls' if os.name == 'nt' else 'clear')
fn = input(Fore.YELLOW + "File Name: " + Fore.RESET)
sepa = "C:\\" if platform.system() == "Windows" else "/"
found = False
for root, dirs, files in os.walk(sepa):
    if fn in files:
        print(Fore.LIGHTGREEN_EX + f"[+] File found: {os.path.join(root, fn)}" + Fore.RESET)
        found = True
if not found:
    print(Fore.RED + "[-] File not found." + Fore.RESET)
