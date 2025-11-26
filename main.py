from adventurelib import *

pockets = []
menu_input = ""

@when ("i")
def inventory():
    print(pockets)

@when ("take THING")
def take(thing):
    pockets.append(thing)
    print(f"You take the {thing}.")

def menu(*args):
    global menu_input
    print("\ni - inventory")
    for arg in args:
        print(f"{arg}")
    menu_input = input()

print("A voice rings out from the blinding void.\nI hope you're prepared.\n")

name = input("What is your name?")

say(f"""
    \n{name}. You are human. You have no choice in the matter. You are stuck like this. 
    You are trapped. You are lesser. You are confined by free will. You are asleep.  

    The void-  not white, not black, no color at all, and yet at the same time crushingly bright- 
    begins to take shape around you. Purples and deep blues greet your eyes, 
    and you find yourself in a cavern lit only by the single torch you carry. It is damp and stuffy. 
    You are asleep. 
""")

menu("A- look around", "B- shut your eyes")
while menu_input != "A" and menu_input != "B" and menu_input != "i":
    print("\nThis is not an option.")
    menu("A- look around", "B- shut your eyes")
if menu_input == "A":
    print("you look around") #expand
elif menu_input == "B":
    print("you shut your eyes") #expand
elif menu_input == "i":
    print(pockets)
else: 
    print("how")

start()

