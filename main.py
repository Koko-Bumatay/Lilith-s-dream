from adventurelib import *

pockets = ["hello"]

@when ("i")
def inventory():
    print(pockets)

@when ("take THING")
def take(thing):
    pockets.append(thing)
    print(f"You take the {thing}.")

def menu(*args):
    print("\ni - inventory")
    for arg in args:
        print(f"{arg}")

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


start()

