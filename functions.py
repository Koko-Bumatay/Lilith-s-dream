from adventurelib import *

def menu(*args):
    global menu_input
    print("\ni - inventory")
    for arg in args:
        print(f"{arg}")
    menu_input = input()

inventory = []


    

menu("A- spit", "B- swallow")
while menu_input != "A" and menu_input != "B" and menu_input != "i":
    print("\nThis is not an option.")
    menu("A- spit", "B- swallow")
if menu_input == "A":
    print("you spit it out")
elif menu_input == "B":
    print("you swallow it")
elif menu_input == "i":
    print(inventory)
else: 
    print("how")