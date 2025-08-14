import os
from random import randint
from time import sleep
from colorama import Fore as fore, Style as style
import colorama

colorama.init(autoreset=True)

def typeWriter(text, colour):
    for i in text:
        print(colour + style.BRIGHT + i, flush=True, end="")
        sleep(0.02)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

dice_faces = [
    """
    ┌─────────┐
    │         │
    │    ●    │
    │         │
    └─────────┘""",
    """
    ┌─────────┐
    │  ●      │
    │         │
    │      ●  │
    └─────────┘""",
    """
    ┌─────────┐
    │  ●      │
    │    ●    │
    │      ●  │
    └─────────┘""",
    """
    ┌─────────┐
    │  ●   ●  │
    │         │
    │  ●   ●  │
    └─────────┘""",
    """
    ┌─────────┐
    │  ●   ●  │
    │    ●    │
    │  ●   ●  │
    └─────────┘""",
    """
    ┌─────────┐
    │  ●   ●  │
    │  ●   ●  │
    │  ●   ●  │
    └─────────┘"""
]

def roll_dice(count):
    for _ in range(count):
        dice = randint(1, 6)
        print(dice_faces[dice-1])

def RollTheDice():
    while True:
        typeWriter("#========== Dice Rolling Simulator ==========#\n\n", fore.YELLOW)
        typeWriter("Enter number of dice (1-10) or '0' to exit: ", fore.CYAN)

        try:
            dice_count = int(input())
        except ValueError:
            typeWriter("Invalid number! Try again.\n", fore.RED)
            sleep(1.5)
            clear_screen()
            continue

        if dice_count == 0:
            return

        if dice_count < 1 or dice_count > 10:
            typeWriter("Please enter between 1 and 10 dice.\n", fore.RED)
            sleep(1.5)
            clear_screen()
            continue

        while True:
            typeWriter("Enter 'r' to roll, 'b' to go back, or 'e' to exit: ", fore.CYAN)
            choice = input().lower()

            if choice == 'r':
                roll_dice(dice_count)
            elif choice == 'b':
                clear_screen()
                break
            elif choice == 'e':
                return
            else:
                typeWriter("Invalid Option! Try Again\n", fore.RED)
                sleep(1.5)
                clear_screen()

if __name__ == "__main__":
    RollTheDice()
