from adventurelib import *
import time
import random

player_health = 10
killcount = 0
pockets = {"Knife": 2, "Sheild": 2, "Apple": 3}

def pause():
    time.sleep(1)

def inventory():
    pause()
    print("\n" + str(list(pockets.keys())))

def take(thing, val):
    pockets[thing] = val
    pause()
    print(f"\nYou take {thing}.")
    return pockets

def menu(*args):
    pause()
    print("\ni - inventory")
    for arg in args:
        pause()
        print(f"{arg}")
    menu_input = input()
    return menu_input
    

def game_start():
    print("************************************************************************************************************")

def game_over():
    print("\nGAME OVER")
    game_start()
