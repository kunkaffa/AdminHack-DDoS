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
