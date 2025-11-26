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

#could this be a loop?
menu("A- look around", "B- shut your eyes")
while menu_input != "A" and menu_input != "B":
    if menu_input == "i":
        print(f"\n{pockets}")
    else:
        print("\nThis is not an option.")
    menu("A- look around", "B- shut your eyes")
if menu_input == "A":
    say("""
        \nYou swivel your head to further examine your surroundings. There appear to be no exits, save for a single tunnel 
        carved into the wall of the cavern, lined with crystals reflecting the light of your torch. You are asleep. 
        Amongst the gleaming gems, you spot eyes. 
    """)
elif menu_input == "B":
    say("""
        You try to close your eyes, but your eyelids won't close. You are already asleep. 
        The darkness you expect to come stays an expectation. 
    """)
    menu("A- look around", "B-shut them tighter")
    while menu_input != "A" and menu_input != "B":
        if menu_input == "i":
            print(f"\n{pockets}")
        else:
            print("\nThis is not an option.")
        menu("A- look around", "B- shut your eyes")
    if menu_input == "A":
        say("""
            \nYou swivel your head to further examine your surroundings. There appear to be no exits, save for a single tunnel 
            carved into the wall of the cavern, lined with crystals reflecting the light of your torch. You are asleep. 
            Amongst the gleaming gems, you spot eyes. 
        """)
    elif menu_input == "B":
        for i in range (30):
            print("You are already asleep.You are already asleep.You are already asleep.")
            #wait for a sec
        #game over
    else:
        print("how")
else: 
    print("how")

print(f"\nFriend: 'Welcome back, {name}. Back so soon?")
menu("A- Welcome back? Have we met?", "I am still asleep")
while menu_input != "A" and menu_input != "B":
    if menu_input == "i":
        print(f"\n{pockets}")
    else:
        print("\nThis is not an option.")
    menu("A- Welcome back? Have we met?", "I am still asleep")
if menu_input == "A":
    say("""
        Friend: 'Of course we have. You are asleep. We have met many times. I know you well. I know that you are human. 
        I know that you wear baggy clothes to cover those strange appendages of yours. I know that you are not what you want to be, 
        and that you are exactly what you want to be'. Friend's teeth bare in a mock grin.  
    """)
elif menu_input == "B":
    print("Friend: 'Shame. Better luck next time around.'")

say("""
    Friend's eyes disappear, and you are left with no memory of their voice. You are asleep. Or of their existence. 
    You press on against the darkness, passing into the corridor of gems. What small amount of sound existed in the main cavern is now 
    gone, and it is entirely silent. The silence is suffocating. You can't even hear your own footsteps. 
    You can only see the torchlight gleaming off the rocks around you, blinding if you look too close. Further down the tunnel, 
    you begin to hear again: footsteps. footsteps you recognize. Not your own. Your father's.
""")

start()

