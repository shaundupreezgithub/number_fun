
import random
import time
import sys
import pyfiglet  # <-- Added for large ASCII banners
# Color codes
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"

def print_header():
    # Use pyfiglet for large ASCII header
    header_banner = pyfiglet.figlet_format("GUESS THE NUMBER")
    print(f"{BOLD}{YELLOW}{header_banner}{RESET}")
def spinner_animation():
    spinner = ["|", "/", "-", "\\"]
    colors = [RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN]
    print("⏳ Checking your guess ", end="", flush=True)
    for _ in range(5):
        for i, frame in enumerate(spinner):
            color = colors[i % len(colors)]
            print(f"\r{color}⏳ Checking your guess {frame}{RESET}", end="", flush=True)
            time.sleep(0.08)
    print("\r", end="")
def fireworks_animation():
    colors = [RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN]
    fireworks = ["✨", "💥", "🔥", "🌟"]
    print("\n")
    for _ in range(10):  # number of fireworks bursts
        line = ""
        for _ in range(33):  # width of the firework line
            color = colors[random.randint(0, len(colors)-1)]
            symbol = fireworks[random.randint(0, len(fireworks)-1)]
            line += f"{color}{symbol}{RESET}"
        print(line)
        time.sleep(0.2)
    print("\n")
def play_game():
    print_header()
    while True:
        num = random.randint(0, 50)
        #print(num)          #optional for testing purposes
        try:
            answer = int(input(f"{YELLOW}👉 Choose your number (00–50): {RESET}"))
        except ValueError:
            print(f"{RED}❌ Please enter a valid number! ❌{RESET}\n")
            continue
        spinner_animation()
        #dots_animation()
        if answer == num:
            # Large ASCII win message
            win_banner = pyfiglet.figlet_format("CONGRATS  !!!")
            print(f"{BOLD}{GREEN}{win_banner}{RESET}")
            champion = pyfiglet.figlet_format("PLEASE PLAY AGAIN SOON  \nGOODBYE  !!! ")
            print(f"{BOLD}{GREEN}{champion}{RESET}")
            fireworks_animation()  # show fireworks 
            #print(champion)
            break
        else:
            print(f"{RED}❌💥 WRONG! The correct number was {num:02d}. Try again! ❌💥{RESET}\n")
play_game()


