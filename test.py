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

def menu(*args):
    global menu_input
    pause()
    print("\ni - inventory")
    for arg in args:
        pause()
        print(f"{arg}")
    menu_input = input()

enemy = "your father"
enemy_max_health = 10
enemy_health = enemy_max_health
aggression = 2 
while enemy_health > 0 and player_health > 0:
    pause()
    print(f"\nPlayer health: {player_health}")
    print(f"Enemy health: {enemy_health}")
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
        damage = random.randint(pockets["Knife"]-1, pockets["Knife"]+1)
        enemy_health -= damage
        pause()
        print(f"\nYou stab {enemy} and deal {damage} damage.")
        damage = random.randint(round(enemy_max_health/2) - 4, round(enemy_max_health/2) - 1)
        player_health -= damage
        pause()
        print(f"\n{enemy} attacks you back, dealing {damage} damage.")
    elif menu_input == "B":
        global block
        block = pockets["Sheild"]
        pause()
        print(f"\nYou raise your sheild. If {enemy} attacks, this will block {block} damage.")
        global counter_flag
        counter_flag = random.randint(0, aggression)
        if counter_flag == 0:
            pause()
            print(f"\n{enemy} did not attack.")
        elif counter_flag > 0:
            damage = random.randint(round(enemy_max_health/2) - 4, round(enemy_max_health/2) -1)
            pause()
            print(f"\n{enemy} attacks you back, dealing {damage} damage. You blocked {block} damage.")
            pause()
            damage -= block
            if damage < 0:
                damage = 0
            else: 
                damage = damage
            player_health -= damage
            print(f"You will take {damage} damage.")
        else:
            print("how")
    elif menu_input == "C":
        pause()
        if player_health == 10:
            print("\nYou cannot heal any further.")
        elif player_health > 7 and player_health < 10:
            global heal
            heal = 10 - player_health 
            print(f"\nYou heal {heal} damage.")
            player_health += heal
        else:
            print("\nYou heal 3 damage.")
            counter_flag = random.randint(0, aggression)
            if counter_flag == 0:
                print(f"\n{enemy} does not attack.")
            elif counter_flag > 0:
                damage = random.randint(round(enemy_max_health/2) - 4, round(enemy_max_health/2) -1)
                player_health -= damage
                print(f"\n{enemy} attacks, dealing {damage} damage.")
    else: 
        print("how")
if player_health > 0:
    print("\nYou win!")
elif player_health <= 0:
    print("\nYou loose.")

start()

