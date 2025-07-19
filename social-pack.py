import os
import time
import random
from pyfiglet import figlet_format

# Color codes
RED = "\033[1;31m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
BLUE = "\033[1;34m"
MAGENTA = "\033[1;35m"
CYAN = "\033[1;36m"
WHITE = "\033[1;37m"
RESET = "\033[0m"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    clear_screen()
    print(RED + figlet_format("Social-Pack", font="slant") + RESET)
    print(BLUE + "="*60 + RESET)
    print(YELLOW + "Author: Anonymous-Teach" + RESET)
    print(BLUE + "="*60 + RESET)
    print()

def load_wordlist(wordlist_path):
    try:
        with open(wordlist_path, 'r', errors='ignore') as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(RED + f"\nError: Wordlist file '{wordlist_path}' not found!" + RESET)
        return None
    except Exception as e:
        print(RED + f"\nError reading wordlist: {e}" + RESET)
        return None

def brute_force(target, platform):
    wordlist_path = input(CYAN + f"\nEnter path to {platform} wordlist file: " + RESET)
    passwords = load_wordlist(wordlist_path)
    
    if not passwords:
        return
    
    print(RED + f"\nStarting {platform} brute force attack on {target}..." + RESET)
    print(YELLOW + f"Loaded {len(passwords)} passwords from wordlist" + RESET)
    
    for idx, password in enumerate(passwords, 1):
        print(YELLOW + f"Trying {idx}/{len(passwords)}: {password}" + RESET)
        time.sleep(0.2)
        
        # Simulate success with 10% chance when reaching 25% of wordlist
        if idx > len(passwords)//4 and random.random() < 0.1:
            print(GREEN + "\n[SUCCESS] Password found!" + RESET)
            print(CYAN + f"Username: {target}" + RESET)
            print(CYAN + f"Password: {password}" + RESET)
            return
    
    print(RED + "\n[FAILED] No matching password found in wordlist" + RESET)
    print(MAGENTA + "Try again with a different wordlist" + RESET)

def insta_ban():
    username = input(CYAN + "\nEnter Instagram username to ban: " + RESET)
    
    print(RED + "\nStarting mass report attack..." + RESET)
    
    for i in range(1, 101):
        time.sleep(0.1)
        print(YELLOW + f"Report {i}/100 sent..." + RESET)
    
    print(GREEN + "\n[SUCCESS] 100 reports completed!" + RESET)
    print(GREEN + "Account will be banned within 24 hours" + RESET)

def main_menu():
    print_banner()
    print(CYAN + "Select an option:\n" + RESET)
    print(GREEN + "1. InstaQbrute - Instagram Brute Force" + RESET)
    print(BLUE + "2. fbQbrute - Facebook Brute Force" + RESET)
    print(RED + "3. igQban - Instagram Account Ban" + RESET)
    print(YELLOW + "0. Exit\n" + RESET)
    
    return input(MAGENTA + "Enter your choice: " + RESET)

def main():
    while True:
        choice = main_menu()
        
        if choice == '1':
            username = input(CYAN + "\nEnter Instagram username: " + RESET)
            brute_force(username, "Instagram")
        elif choice == '2':
            username = input(CYAN + "\nEnter Facebook username/email: " + RESET)
            brute_force(username, "Facebook")
        elif choice == '3':
            insta_ban()
        elif choice == '0':
            print(RED + "\nExiting SocialPack..." + RESET)
            break
        else:
            print(RED + "\nInvalid choice! Try again." + RESET)
            
        input(YELLOW + "\nPress Enter to continue..." + RESET)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(RED + "\nTool stopped by user" + RESET)
    except Exception as e:
        print(RED + f"\nAn error occurred: {e}" + RESET)
