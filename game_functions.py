from adventurelib import *
import time
import random

player_health = 15
killcount = 0
pockets = {"Knife": 3, "Sheild": 2, "A bag of apples that only refills at the end of a battle": 3}
heal = pockets["A bag of apples that only refills at the end of a battle"]

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

#this prints out a menu of options and allows the user to choose
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
    exit()

#fight sequence
def fight(enemy, enemy_health, aggression, heal_count):
    global player_health
    global player_max_health
    player_max_health = player_health
    global enemy_max_health
    enemy_max_health = enemy_health
    #checks if player and enemy are alive
    while enemy_health > 0 and player_health > 0:
        pause()
        print(f"\nPlayer health: {player_health}")
        print(f"Enemy health: {enemy_health}")
        menu_input = menu("A- attack", "B- block", "C- eat an apple")
        #if a player does not enter any of the three options, it checks if they asked for inventory or if they typed something that is not an option
        while menu_input != "A" and menu_input != "B" and menu_input != "C": 
            if menu_input == "i":
                inventory()
            else:
                pause()
                print("\nThis is not an option.")
            menu_input = menu("A- attack", "B- block", "C- eat an apple")
        #if they choose to attack, it calculates the damage and applies it to the enemy
        if menu_input == "A":
            global damage
            #calculates damage in a range between +1 and -1 of the base stat
            damage = random.randint(pockets["Knife"]-1, pockets["Knife"]+1)
            enemy_health -= damage
            pause()
            print(f"\nYou stab {enemy} and deal {damage} damage.")
            #the enemy then counters, and their damage is in a range around half their health 
            damage = random.randint(round(enemy_max_health/2) - 4, round(enemy_max_health/2) - 1)
            player_health -= damage
            pause()
            print(f"\n{enemy} attacks you back, dealing {damage} damage.")
        #if the player chooses to sheild themselves, it can block incoming damage once they are out of heals
        elif menu_input == "B":
            global block
            block = pockets["Sheild"]
            pause()
            print(f"\nYou raise your sheild. If {enemy} attacks, this will block {block} damage.")
            #determines if the enemy will counterattack depending on their aggression
            global counter_flag
            counter_flag = random.randint(0, aggression)
            if counter_flag == 0:
                pause()
                print(f"\n{enemy} did not attack.")
            elif counter_flag > 0:
                #calculates damage in a range around a third of the enemy health 
                damage = random.randint(round(enemy_max_health/3) - 4, round(enemy_max_health/3) -1)
                pause()
                print(f"\n{enemy} attacks you back, dealing {damage} damage. You blocked {block} damage.")
                pause()
                #this calculates the damage dealt versus the damage blocked
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
            global heal
            pause()
            #checks if heals remain
            if heal_count == 0:
                print("\nYou have no more heals. Heals will be replenished at the start of the next battle.")
            elif heal_count > 0:
                if player_health == player_max_health:
                    print("\nYou cannot heal any further.")
                #this makes it so you can't heal past max health
                elif player_health > player_max_health - heal and player_health < player_max_health:
                    heal = player_max_health - player_health 
                    print(f"\nYou heal {heal} damage.")
                    player_health += heal
                    heal_count -= 1
                    print(f"You have {heal_count} heals left.")
                else:
                    print(f"\nYou heal {heal} damage.")
                    player_health += heal
                    heal_count -= 1
                    print(f"You have {heal_count} heals left.")
                #like in block, it determines if the enemy counters based on aggression
                counter_flag = random.randint(0, aggression)
                if counter_flag == 0:
                    print(f"\n{enemy} does not attack.")
                elif counter_flag > 0:
                    #calculates damage in a range around a third of the enemy health 
                    damage = random.randint(round(enemy_max_health/3) - 4, round(enemy_max_health/3) -1)
                    player_health -= damage
                    print(f"\n{enemy} attacks, dealing {damage} damage.")
                else:
                    print("how")
            else:
                print("how")
        else: 
            print("how")
    if player_health > 0:
        print("\nYou win!")
        global killcount
        killcount += 1
        player_health = player_max_health
    elif player_health <= 0:
        print("\nYou lose.")
        game_over()

#final boss fight sequence
def lilith_fight():
    global player_health
    global player_max_health
    player_max_health = player_health
    global enemy_max_health
    enemy_max_health = 40
    enemy_health = enemy_max_health
    heal_count = 5
    while enemy_health > 0 and player_health > 0:
        pause()
        print(f"\nPlayer health: {player_health}")
        print(f"Enemy health: {enemy_health}")
        menu_input = menu("A- attack", "B- block", "C- eat an apple")
        #if a player does not enter any of the three options, it checks if they asked for inventory or if they typed something that is not an option
        while menu_input != "A" and menu_input != "B" and menu_input != "C": 
            if menu_input == "i":
                inventory()
            else:
                pause()
                print("\nThis is not an option.")
            menu_input = menu("A- attack", "B- block", "C- eat an apple")
        #if they choose to attack, it calculates the damage in a -1 to +2 range of the base stat
        if menu_input == "A":
            global damage
            damage = random.randint(pockets["Knife"]-1, pockets["Knife"]+2)
            enemy_health -= damage
            pause()
            print(f"\nYou stab Lilith and deal {damage} damage.")
            #the enemy then counters, and their damage is in a range from 5 to 9 
            damage = random.randint(5, 9)
            player_health -= damage
            pause()
            print(f"\nLilith attacks you back, dealing {damage} damage.")
        #if the player chooses to sheild themselves, it can block incoming damage once they are out of heals
        elif menu_input == "B":
            global block
            block = pockets["Sheild"]
            pause()
            print(f"\nYou raise your sheild. If Lilith attacks, this will block {block} damage.")
            #it determines if the enemy will counterattack in a range of 0 to 8
            global counter_flag
            counter_flag = random.randint(0, 8)
            if counter_flag == 0:
                pause()
                print(f"\nLilith did not attack.")
            elif counter_flag > 0:
                #calculates damage in a range from 3 to 9
                damage = random.randint(3, 9)
                pause()
                print(f"\nLilith attacks you back, dealing {damage} damage. You blocked {block} damage.")
                pause()
                #this calculates the damage dealt versus the damage blocked
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
            global heal
            pause()
            #checks if heals remain
            if heal_count == 0:
                print("\nYou have no more heals. Heals will be replenished at the start of the next battle.")
            elif heal_count > 0:
                if player_health == player_max_health:
                    print("\nYou cannot heal any further.")
                #this makes it so you can't heal past max health
                elif player_health > player_max_health - heal and player_health < player_max_health:
                    heal = player_max_health - player_health 
                    print(f"\nYou heal {heal} damage.")
                    player_health += heal
                    heal_count -= 1
                    print(f"You have {heal_count} heals left.")
                else:
                    print(f"\nYou heal {heal} damage.")
                    player_health += heal
                    heal_count -= 1
                    print(f"You have {heal_count} heals left.")
                #like in block, it determines if the enemy counters in a range of 0 to 8
                counter_flag = random.randint(0, 8)
                if counter_flag == 0:
                    print(f"\nLilith does not attack.")
                elif counter_flag > 0:
                    damage = random.randint(2, 4)
                    player_health -= damage
                    print(f"\nLilith attacks, dealing {damage} damage.")
                else:
                    print("how")
            else:
                print("how")
        else: 
            print("how")
    if player_health > 0:
        print("\nYou win!")
        global killcount
        killcount += 1
        player_health = player_max_health
    elif player_health <= 0:
        print("\nYou lose.")
        game_over()
