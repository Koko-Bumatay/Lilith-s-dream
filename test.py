def menu(*args):
    global menu_input
    print("\ni - inventory")
    for arg in args:
        print(f"{arg}")
    menu_input = input()

pockets = []

menu("A- look around", "B- shut your eyes")
while menu_input != "A" and menu_input != "B":
    if menu_input == "i":
        print(f"\n{pockets}")
    else:
        print("\nThis is not an option.")
    menu("A- look around", "B- shut your eyes")
if menu_input == "A":
    print("""
        \nYou swivel your head to further examine your surroundings. There appear to be no exits, save for a single tunnel 
        carved into the wall of the cavern, lined with crystals reflecting the light of your torch. You are asleep. 
        Amongst the gleaming gems, you spot eyes. 
    """)
elif menu_input == "B":
    print("""
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
        print("""
            \nYou swivel your head to further examine your surroundings. There appear to be no exits, save for a single tunnel 
            carved into the wall of the cavern, lined with crystals reflecting the light of your torch. You are asleep. 
            Amongst the gleaming gems, you spot eyes. 
        """)
    elif menu_input == "B":
        for i in range (30):
            print("You are already asleep.You are already asleep.You are already asleep.")
        #game over
    else:
        print("how")
else: 
    print("how")