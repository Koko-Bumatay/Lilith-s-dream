from adventurelib import *
import time 
import random

player_health = 10
killcount = 0
pockets = {"Knife": 2, "Sheild": 2, "Apple": 3}

def inventory():
    pause()
    print(list(pockets.keys()))

def pause():
    time.sleep(1)

def menu(*args):
    global menu_input
    pause()
    print("\ni - inventory")
    for arg in args:
        pause()
        print(f"{arg}")
    menu_input = input()

enemy = "your father"
enemy_health = 10
menu("A- attack", "B- block", "C- heal")
while menu_input != "A" and menu_input != "B" and menu_input != "C":
    if menu_input == "i":
        inventory()
    else:
        pause()
        print("\nThis is not an option.")
    menu("A- attack", "B- block", "C- heal")
if menu_input == "A":
    global damage
    damage = random.randint(pockets["Knife"]-1,pockets["Knife"]+1)
    enemy_health -= damage
    pause()
    print(f"\nYou stab {enemy} and deal {damage} damage.")
elif menu_input == "B":
    pause()
    print("\nYou raise your sheild. If the enemy attacks, this will block 2 damage.")
elif menu_input == "C":
    pause()
    if player_health == 10:
        print("\nYou cannot heal any further. You do not get your turn back.")
    elif player_health >= 7 and player_health <= 10:
        global heal
        heal = 10 - player_health 
        print(f"\nYou heal {heal} damage.")
        player_health += heal
    else:
        print("\n You heal 3 damage.")
else: 
    print("how")

start()

