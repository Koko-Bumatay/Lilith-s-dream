from adventurelib import *

pockets = []

@when ("i")
def inventory():
    print(pockets)

@when ("take THING")
def take(thing):
    pockets.append(thing)
    print(f"\nYou take {thing}.")

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
menu("A- Welcome back? Have we met?", "B- I am still asleep")
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

menu("A- approach", "B- do not approach")
while menu_input != "A" and menu_input != "B":
    if menu_input == "i":
        print(f"\n{pockets}")
    else:
        print("\nThis is not an option.")
    menu("A- ", "B- ")
if menu_input == "A":
    say("""
        He growls as you come close, ears twitching, tail slightly tucked. He knows what you are, and he is ashamed of it. 
        You are human. You are asleep. He will make you animal if it's the last thing he does.
    """)
elif menu_input == "B":
    say("""
        You crouch, and stay back, wary of the animal in front of you. As you lower yourself, he approaches you, 
        a longing in his eyes and a warning in his throat. You are asleep, You are human, and he hates it. He attacks you, 
        teeth ripping flesh off bone, mercilessly unmaking you. You remain asleep.
    """)
    #game over
else:
    print("how")

#fight with father 

say("""
    As you deliver the final blow to your father's bloodied form, dropping your torch to the ground, 
    you feel part of your humanity slipping away from you. You reach for it, but you cannot see with the torch behind you. 
    You cannot regain this humanity. You know what you are. You are asleep. Your father bleeds on the shining crystals, 
    staining the mirrors of the flickering torch. You press on against the darkness. You will not mourn. 
    After walking for what seems like forever and no time at all, you find yourself out of the crystal tunnel, emerging into a forest. 
    Deep greens fill your vision, amorphous clumps of leaf and limb occupy your surroundings, 
    and the sound of a river in the distance finds your ears. Someone with light brown fur presents themself in front of you, 
    and you recognize it to be your mother.  
""")

menu("A- attack", "B- approach gently")
while menu_input != "A" and menu_input != "B":
    if menu_input == "i":
        print(f"\n{pockets}")
    else:
        print("\nThis is not an option.")
    menu("A- ", "B- ")
if menu_input == "A":
    say("""
        You are swift this time. You know how this goes. [fight] You kick your mother's crumpled body aside. 
        Another piece of your humanity is gone, and the absence is intoxicating. But you remain asleep.
    """)
elif menu_input == "B":
    say("""
        You approach your mother with your hand out for her to smell, and she nuzzles you. In her eyes is a sadness, 
        and you know that she, too, wishes you were other than that which you are. You are still asleep. She kneels at your feet. 
        Suddenly, she begins to wither, her skin melting first, revealing a ribcage sheltering a crumbling violet, petals drooping. 
        Eventually, her bones crumble too, leaving only the flower behind.  
    """)
    menu("A- take flower", "B- leave it")
    while menu_input != "A" and menu_input != "B":
        if menu_input == "i":
            print(f"\n{pockets}")
        else:
            print("\nThis is not an option.")
        menu("A- ", "B- ")
    if menu_input == "A":
        take("Lilith's flower")
    elif menu_input == "B":
        print("You leave it on the ground.")
    else:
        print("how")
else:
    print("how")

say("""
    Striding forward past your mother's once physical form, your attention is called back to the path you walk. 
    Looking forward, you can make out a fork in the road. To your left, the path becomes blood red, and the stench of rot wafts forth. 
    You are asleep. To your right, the path continues, but the dwindling light provided by your torch fails to unveil anything more. 
    A fog creeps into your small circle of visibility from the darkness.  
""")

menu("A- go left", "B- go right")
while menu_input != "A" and menu_input != "B":
    if menu_input == "i":
        print(f"\n{pockets}")
    else:
        print("\nThis is not an option.")
    menu("A- ", "B- ")
if menu_input == "A":
    
elif menu_input == "B":

start()

