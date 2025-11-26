from adventurelib import *

def menu(*args):
    global menu_input
    print("\ni - inventory")
    for arg in args:
        print(f"{arg}")
    menu_input = input()