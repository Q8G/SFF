import os, platform
from colorama import init, Fore
init()
os.system("title Soul Files Finder")
os.system('cls' if os.name == 'nt' else 'clear')
filename = input(Fore.YELLOW + "File Name: " + Fore.RESET)
search_path = "C:\\" if platform.system() == "Windows" else "/"
found = False
for root, dirs, files in os.walk(search_path):
    if filename in files:
        print(Fore.LIGHTGREEN_EX + f"[+] File found: {os.path.join(root, filename)}" + Fore.RESET)
        found = True
if not found:
    print(Fore.RED + "[-] File not found." + Fore.RESET)
