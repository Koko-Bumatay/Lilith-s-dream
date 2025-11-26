def menu(*args):
    global menu_input
    print("\ni - inventory")
    for arg in args:
        print(f"{arg}")
    menu_input = input()

pockets = []

menu("A- ", "B- ")
while menu_input != "A" and menu_input != "B":
    if menu_input == "i":
        print(f"\n{pockets}")
    else:
        print("\nThis is not an option.")
    menu("A- ", "B- ")
if menu_input == "A":
    
elif menu_input == "B":

else:
    print("how")

