from functions import *

def menu(*args):
    pause()
    print("\ni - inventory")
    for arg in args:
        pause()
        print(f"{arg}")
    menu_input = input()
    return menu_input



def fight(enemy, enemy_health, aggression, heal_count):
    global player_health
    global player_max_health
    player_max_health = player_health
    global enemy_max_health
    enemy_max_health = enemy_health
    while enemy_health > 0 and player_health > 0:
        pause()
        print(f"\nPlayer health: {player_health}")
        print(f"Enemy health: {enemy_health}")
        menu_input = menu("A- attack", "B- block", "C- eat an apple")
        while menu_input != "A" and menu_input != "B" and menu_input != "C":
            if menu_input == "i":
                inventory()
            else:
                pause()
                print("\nThis is not an option.")
            menu_input = menu("A- attack", "B- block", "C- eat an apple")
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
            if heal_count == 0:
                print("\nYou have no more heals. Heals will be replenished at the start of the next battle.")
            elif heal_count > 0:
                if player_health == player_max_health:
                    print("\nYou cannot heal any further.")
                elif player_health > player_max_health - 3 and player_health < player_max_health:
                    global heal
                    heal = player_max_health - player_health 
                    print(f"\nYou heal {heal} damage.")
                    player_health += heal
                    heal_count -= 1
                    print(f"You have {heal_count} heals left.")
                else:
                    print("\nYou heal 3 damage.")
                    player_health += 3
                    heal_count -= 1
                    print(f"You have {heal_count} heals left.")
                counter_flag = random.randint(0, aggression)
                if counter_flag == 0:
                    print(f"\n{enemy} does not attack.")
                elif counter_flag > 0:
                    damage = random.randint(round(enemy_max_health/2) - 4, round(enemy_max_health/2) -1)
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
        #killcount += 1
        player_health = player_max_health
    elif player_health <= 0:
        print("\nYou lose.")
        game_over()
        exit()

fight("test", 1, 2, 3)
start()