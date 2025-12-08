from game_functions import *

game_start()

killcount = 0

print("A voice rings out from the blinding void.\nI hope you're prepared.\n")

pause()
name = input("What is your name?")

pause()
say(f"""
    \n{name}. You are human. You have no choice in the matter. You are stuck like this. 
    You are trapped. You are lesser. You are confined by free will. You are asleep.  

    The void-  not white, not black, no color at all, and yet at the same time crushingly bright- 
    begins to take shape around you. Purples and deep blues greet your eyes, 
    and you find yourself in a cavern lit only by the single torch you carry. It is damp and stuffy. 
    You are asleep. 
""")

#prints the menu and takes different actions depending on the response
pause()
menu_input = menu("A- look around", "B- shut your eyes")
while menu_input != "A" and menu_input != "B":
    if menu_input == "i":
        inventory()
    else:
        pause()
        print("\nThis is not an option.")
    menu_input = menu("A- look around", "B- shut your eyes")
if menu_input == "A":
    pause()
    say("""
        \nYou swivel your head to further examine your surroundings. There appear to be no exits, save for a single tunnel 
        carved into the wall of the cavern, lined with crystals reflecting the light of your torch. You are asleep. 
        Amongst the gleaming gems, you spot eyes. 
    """)
elif menu_input == "B":
    pause()
    say("""
        \nYou try to close your eyes, but your eyelids won't close. You are already asleep. 
        The darkness you expect to come stays an expectation. 
    """)
    menu_input = menu("A- look around", "B- shut them tighter")
    while menu_input != "A" and menu_input != "B":
        if menu_input == "i":
            inventory()
        else:
            pause()
            print("\nThis is not an option.")
        menu_input = menu("A- look around", "B- shut your eyes")
    if menu_input == "A":
        pause()
        say("""
            \nYou swivel your head to further examine your surroundings. There appear to be no exits, save for a single tunnel 
            carved into the wall of the cavern, lined with crystals reflecting the light of your torch. You are asleep. 
            Amongst the gleaming gems, you spot eyes. 
        """)
    elif menu_input == "B":
        pause()
        for i in range (30):
            time.sleep(.25)
            print("You are already asleep.You are already asleep.You are already asleep.")
        game_over()
    else:
        print("how")
else: 
    print("how")

print(f"\nFriend: 'Welcome back, {name}. Back so soon?'")
menu_input = menu("A- Welcome back? Have we met?", "B- I am still asleep")
while menu_input != "A" and menu_input != "B":
    if menu_input == "i":
        inventory()
    else:
        pause()
        print("\nThis is not an option.")
    menu_input = menu("A- Welcome back? Have we met?", "I am still asleep")
if menu_input == "A":
    pause()
    say("""
        \nFriend: 'Of course we have. You are asleep. We have met many times. I know you well. I know that you are human. 
        I know that you wear baggy clothes to cover those strange appendages of yours. I know that you are not what you want to be, 
        and that you are exactly what you want to be'. Friend's teeth bare in a mock grin.  
    """)
elif menu_input == "B":
    pause()
    print("\nFriend: 'Shame. Better luck next time around.'")

pause()
say("""
    \nFriend's eyes disappear, and you are left with no memory of their voice. You are asleep. Or of their existence. 
    You press on against the darkness, passing into the corridor of gems. What small amount of sound existed in the main cavern is now 
    gone, and it is entirely silent. The silence is suffocating. You can't even hear your own footsteps. 
    You can only see the torchlight gleaming off the rocks around you, blinding if you look too close. Further down the tunnel, 
    you begin to hear again: footsteps. footsteps you recognize. Not your own. Your father's.
""")

menu_input = menu("A- approach", "B- do not approach")
while menu_input != "A" and menu_input != "B":
    if menu_input == "i":
        inventory()
    else:
        pause()
        print("\nThis is not an option.")
    menu_input = menu("A- approach", "B- do not approach")
if menu_input == "A":
    pause()
    say("""
        \nHe growls as you come close, ears twitching, tail slightly tucked. He knows what you are, and he is ashamed of it. 
        You are human. You are asleep. He will make you animal if it's the last thing he does.
    """)
elif menu_input == "B":
    pause()
    say("""
        \nYou crouch, and stay back, wary of the animal in front of you. As you lower yourself, he approaches you, 
        a longing in his eyes and a warning in his throat. You are asleep, You are human, and he hates it. He attacks you, 
        teeth ripping flesh off bone, mercilessly unmaking you. You remain asleep.
    """)
    game_over()
else:
    print("how")

#a fight with "your father" who has 10 health and 3 agression
fight("your father", 10, 3, 3)

pause()
say("""
    \nAs you deliver the final blow to your father's bloodied form, dropping your torch to the ground, 
    you feel part of your humanity slipping away from you. You reach for it, but you cannot see with the torch behind you. 
    You cannot regain this humanity. You know what you are. You are asleep. Your father bleeds on the shining crystals, 
    staining the mirrors of the flickering torch. You press on against the darkness. You will not mourn. 
    After walking for what seems like forever and no time at all, you find yourself out of the crystal tunnel, emerging into a forest. 
    Deep greens fill your vision, amorphous clumps of leaf and limb occupy your surroundings, 
    and the sound of a river in the distance finds your ears. Someone with light brown fur presents themself in front of you, 
    and you recognize it to be your mother.  
""")

menu_input = menu("A- attack", "B- approach gently")
while menu_input != "A" and menu_input != "B":
    if menu_input == "i":
        inventory()
    else:
        pause()
        print("\nThis is not an option.")
    menu_input = menu("A- attack", "B- approach gently")
if menu_input == "A":
    pause()
    say("""
        \nYou are swift this time. You know how this goes.
    """)

    fight("your mother", 8, 1, 3)

    say("""
        \nYou kick your mother's crumpled body aside. 
        Another piece of your humanity is gone, and the absence is intoxicating. But you remain asleep.
    """)
elif menu_input == "B":
    pause()
    say("""
        \nYou approach your mother with your hand out for her to smell, and she nuzzles you. In her eyes is a sadness, 
        and you know that she, too, wishes you were other than that which you are. You are still asleep. She kneels at your feet. 
        Suddenly, she begins to wither, her skin melting first, revealing a ribcage sheltering a crumbling violet, petals drooping. 
        Eventually, her bones crumble too, leaving only the flower behind.  
    """)
    #adds a lilith key to the inventory
    menu_input = menu("A- take flower", "B- leave it")
    while menu_input != "A" and menu_input != "B":
        if menu_input == "i":
            inventory()
        else:
            pause()
            print("\nThis is not an option.")
        menu_input = menu("A- take flower", "B- leave it")
    if menu_input == "A":
        take("Lilith's flower", 0)
    elif menu_input == "B":
        pause()
        print("You leave it on the ground.")
    else:
        print("how")
else:
    print("how")

pause()
say("""
    \nStriding forward past your mother's once physical form, your attention is called back to the path you walk. 
    Looking forward, you can make out a fork in the road. To your left, the path becomes blood red, and the stench of rot wafts forth. 
    You are asleep. To your right, the path continues, but the dwindling light provided by your torch fails to unveil anything more. 
    A fog creeps into your small circle of visibility from the darkness.  
""")

menu_input = menu("A- go left", "B- go right")
while menu_input != "A" and menu_input != "B":
    if menu_input == "i":
        inventory()
    else:
        pause()
        print("\nThis is not an option.")
    menu_input = menu("A- go left", "B- go right")
if menu_input == "A":
    global path_choice
    path_choice = "left"
    pause()
    say("""
        \nYou step towards the scent of viscera. Pressing forward along the leftward path, the stench becoming unbearable, 
        you find yourself ankle-deep in bloodred puddles that reflect your flame, inconsequential to the blindness of your sleep. 
        As your trembling legs ambulate, you stumble over something you cannot see. This dark thing begins to shift, 
        seemingly awoken by your stepping on it, and arranges itself upright. Towering over you, 
        this wall of something deeper than black begins to edge forward, almost consuming the bloodied ground in front of you.  
    """)
    
    menu_input = menu("A- fight", "B- flight", "C- freeze")
    while menu_input != "A" and menu_input != "B" and menu_input != "C":
        if menu_input == "i":
            inventory()
        else:
            pause()
            print("\nThis is not an option.")
        menu_input = menu("A- fight", "B- flight", "C- freeze")
    if menu_input == "A":
        fight("the dark thing", 12, 3, 3)
    elif menu_input == "B":
        pause()
        say("""
            \nYou scramble backwards, longing for the pressing comfort of the cavern you began in. 
            Gripping rock and bone and gore to aid your escape, you find yourself widening the distance between you and the dark thing. 
            You continue to sprint, to climb, to crawl, only to find yourself suddenly consumed by the void that is beyond darkness. 
            Suffocating, scraping invisible appendages rip you in different directions, almost eating you whole. You remain asleep.
        """)
        game_over()
    elif menu_input == "C":
        pause()
        say("""
            \nA deep, ancient terror unfurls inside you starting at the pit of your stomach. You are rooted in place, 
            not able to fight nor run nor even scream. As the dark thing inches towards you, 
            you lose your sense of up and down and left and right, this mass is not defined by direction. 
            You find yourself suddenly consumed by the void that is beyond darkness. Suffocating, 
            scraping invisible appendages rip you in different directions, almost eating you whole. You remain asleep. 
        """)
        game_over()

    pause()
    say("""
        \nWiping the oozing gore of the dark thing from your body, you begin to move. Shaken by the conflict, 
        you consider curling up and lying in the damp stench of the dead and capitulating to the dread. But you can't stop now. 
        With your latest murder you felt another cord of the rope connecting you to humanity snap, and you relished it. It felt... 
        exciting. But you are still asleep. Reflecting on this feeling, you walk further forward, hunting. 
        You find your next brush with death in the form of a great bear-like beast, protecting its young. 
        As you stride towards the family, stomping through the blood-puddles, you begin to pause.  
    """)

    menu_input = menu("A- fight", "B- atone")
    while menu_input != "A" and menu_input != "B":
        if menu_input == "i":
            inventory()
        else:
            pause()
            print("\nThis is not an option.")
        menu_input = menu("A- fight", "B- atone")
    if menu_input == "A":
        fight("the beast", 12, 10, 3)
    elif menu_input == "B":
        pause()
        say("""
            \nThe beast swivels its head, recognizing the threat you pose. You paused for too long. It pounces forward, 
            standing between its young and you, growling. You try to back down, to signal for peace, but you cannot undo this. 
            The beast leaps onto you, biting chunks from your flesh and mauling you asunder with its paws. 
            The final blow comes with a powerful tear, and the creature severs your head from your torso. In your final moments, 
            you see the younger beasts dragging your body towards their den. You remain asleep.
        """)
        game_over()
    else:
        print("how")

    pause()
    say("""
        \nThe body of the beast falls to the ground, gutted and torn. With it, you feel yet another part of your humanity fall away, 
        but with it comes no more pleasure. Instead, the horror of your choices begins to set in. Examining your surroundings closer, 
        you see that the bear's guts are not the only ones that coat the ground. Bones and organs are all around you, 
        glistening in your torchlight, and the blood has stained the skin on your legs. You are asleep. A deep repulsion washes over you, 
        and you begin to vomit. Buckling over, you heave volume after volume of gore from your stomach that couldn't possibly 
        have been truly inside you. In your wretched retching, you feel a clammy hand pat at your back.  
    """)

    menu_input = menu("A- execution", "B- stasis")
    while menu_input != "A" and menu_input != "B":
        if menu_input == "i":
            inventory()
        else:
            pause()
            print("\nThis is not an option.")
        menu_input = menu("A- execution", "B- stasis")
    if menu_input == "A":
        fight("the other you", 15, 4, 3)
    elif menu_input == "B":
        pause()
        say("""
            \nThe cold limb caresses you, and you whip around to find its owner. It belongs to someone that looks just like you. 
            Every feature, strand of hair, and blemish on your form is mirrored on this person'. You prepare to run for your life, 
            but they cling onto you, embracing you tightly. Their form begins to meld to yours, 
            skin grafting and rearranging until fully combined with your own. You are now an amalgamation of two versions of yourself, 
            limbs and eyes on your body without a line of reason or axis of symmetry. When you attempt to scream, 
            you find the choice of which mouth to use overwhelming. It takes what feels like years to learn how to walk again, 
            how to process the sensory information flooding your brain. You are asleep. But eventually, 
            you find yourself able to move about how you did before, and you gain a sense of bolstered confidence, 
            as if you have become stronger.\nYou now have 25 health.\nYour knife's base attack is now 4.
            \nYour sheild's block is now 4.\nYou now have 5 apples per battle.
            \nYou continue forward, more determined than before.
        """)
        #makes items and player stronger
        pockets["Knife"] = 7
        pockets["Sheild"] = 7
        pockets["A bag of apples that only refills at the end of a battle"] = 7
        player_health = 20
    else:
        print("how")
elif menu_input == "B":
    path_choice = "right"
    pause()
    say(f"""
        \nYou step towards the black fog. Continuing forward, you find yourself surrounded by it. Tendrils of the stuff arc towards you, 
        almost reaching out. You reach out your arm in response, and it wraps around you. It's in your nose, your mouth, your lungs, 
        your eyes, suffocating you. You are asleep. You can't breathe, scream, or see, and when the burning in your chest stops, 
        you find yourself blinded. Whether your torch went out or the fog stole your sight from you, 
        you find it impossible to make out your surroundings. You begin to stumble, 
        trying to stay balanced on a surface that you think is the ground, but your spatial sense have failed you. 
        You fall to the ground, flailing in the darkness. As you lie, unable to move, something begins to materialize in your vision, 
        something you can finally see. A pair of eyes blink back at you. You recognize it to be Friend. 
        The tendrils begin to release their iron grip on you, allowing you to breathe again. 

        Friend: 'Nice to see you again, {name}. I see you're close to waking up. I know what lies in the future of your path, 
        and you do too. We both know that you're not strong enough as you are. We both know what you are. So, I have a proposal for you. 
        I can steal the rest of your humanity, if you're able to pass my own test... or you could just walk away now.' Friend smiles. 
        'I think we both know there's really only one option, unless you're interested in meeting again. 
        I advise you break the cycle. You need to wake up.' 
    """)

    menu_input = menu("A- wake up", "B- stay asleep")
    while menu_input != "A" and menu_input != "B":
        if menu_input == "i":
            inventory()
        else:
            pause()
            print("\nThis is not an option.")
        menu_input = menu("A- wake up", "B- stay asleep")
    if menu_input == "A":
        pause()
        say(f"""
            Friend: 'Alright then. I'll grant you the power you need to finally move on to the next life, but only on one condition. 
            You must tell me, honestly, who you are. If I find you dishonest, you'll have to try again. From the beginning. 
            So, who is {name}?” 
        """)

        menu_input = menu("A- A good person. No matter how many mistakes I've made, I've still tried my hardest my whole life. I love those that surround me, and I make sure to show them that. I am a good person.", 
             "B- A flawed person. I try to do the best I can, but inside me lays dormant an anger that can't be contained forever, the scared anger of a wounded animal. I am a flawed person.", 
             "C-  I don't know who I am. I have only lived this life once through, not enough to know every part of myself. Ive made no impact on the world, nothing changes because of my existence. I am nobody at all.")
        while menu_input != "A" and menu_input != "B" and menu_input != "C":
            if menu_input == "i":
                inventory()
            else:
                pause()
                print("\nThis is not an option.")
            menu_input = menu("A- A good person. No matter how many mistakes I've made, I've still tried my hardest my whole life. I love those that surround me, and I make sure to show them that. I am a good person.", 
                 "B- A flawed person. I try to do the best I can, but inside me lays dormant an anger that can't be contained forever, the scared anger of a wounded animal. I am a flawed person.", 
                 "C-  I don't know who I am. I have only lived this life once through, not enough to know every part of myself. Ive made no impact on the world, nothing changes because of my existence. I am nobody at all.")
        if menu_input == "A":
            pause()
            say("""
                \nFriend: 'You're wrong, and you know it. Would the dreamscape of a 'good person' look like this?' 
                The tendrils restrict around you again, this time burning you even more. 
                It feels like every orifice in your body is stuffed with the thick, unbreathable fog, 
                and what little you could see begins to fade away. You remain asleep.
            """)
            game_over()
        elif menu_input == "B":
            pause()
            say("""
                \nFriend: 'Correct. I'm glad that you're finally starting to wake up.' The tendrils once again impale you, 
                this time through your chest. A searing pain arcs through every vein, liquid fire coursing through you. 
                When the searing finally subsides, you feel as if the burning had stolen what was left of your humanity. 
                A bestial roar bubbles up in your chest, and as it escapes you the fog begins to dissipate.
                \nYou now have 25 health.\nYour knife's base damage is now 4.\nYour sheild's block is now 4.\nYou now have 5 apples per battle.
                \nYou stumble your way to your feet, 
                and see your torch, still flickering on the ground. After picking it up, you continue on the dimly lit path, 
                slightly more determined than before.
            """)
            #makes the items and player stronger
            pockets["Knife"] = 7
            pockets["Sheild"] = 7
            pockets["A bag of apples that only refills at the end of a battle"] = 7
            player_health = 20
        elif menu_input == "C":
            pause()
            say("""
                \nFriend: 'Don't lie to yourself. Positive or negative, we all make change in our own reality. It seems you need to go back, 
                and pay better attention to your life this time around.' The tendrils restrict around you again, 
                this time burning you even more. It feels like every orifice in your body is stuffed with the thick, unbreathable fog, 
                and what little you could see begins to fade away. You remain asleep.
            """)
            game_over()
        else:
            print("how")
    elif menu_input == "B":
        pause()
        say("""
            \nFriend: 'If you say so.' The tendrils restrict around you again, this time burning you even more. 
            It feels like every orifice in your body is stuffed with the thick, unbreathable fog, 
            and what little you could see begins to fade away.
        """)
        game_over()
    else:
        print("how")
else:
    print("how")

pause()
say("""
    \nTraveling further forward, you find yourself in a lighter domain, the ground covered in various glistening animal skulls. 
    On the nearly polished surfaces you see hundreds, thousands, millions of reflections of yourself. 
    Two great ivory pillars tower on either side of an equally huge causeway over a raging, wine-dark river. 
    Above the gate at the end of the causeway hangs a gigantic granite block with the symbol of Lilith inscribed on it. 
    You feel awe overtake you, causing you to pause in your movement.  
""")

menu_input = menu("A- stop here", "B- press forward")
while menu_input != "A" and menu_input != "B":
    if menu_input == "i":
        inventory()
    else:
        pause()
        print("\nThis is not an option.")
    menu_input = menu("A- stop here", "B- press forward")
if menu_input == "A":
    pause()
    say("""
        \nThe awe has filled every fiber in your body. Heart-taking, heart-stopping, life-taking awe. You find yourself rooted to the ground, 
        completely unable to move. As you struggle harder against your stasis, the awe that fills you is replaced with terror. Everything is your fault, 
        and nothing will change. Despite your efforts, you remain asleep.
    """)
    game_over()
elif menu_input == "B":
    pause()
    print("\nYou are moving on. There is no going back. There is no changing the choices you've made.")
else:
    print("how")

#ending check based on killcount, path choice, and the presence of the lilith flower
if killcount == 1 and "Lilith's flower" not in pockets:
    pause()
    say("""
        \nYou slowly manage to move one leg forward. Then another. Step after step, you slowly make your way to the massive pillars, gaining speed as you go. 
        Before you know it, you are sprinting. You don't know why. You are so close to waking up. As you reach the base of the pillars, your surroundings suddenly disappear. 
        You are in pure, dark, void. You can see nothing. You wave your hands in front of your face to test if you can see anything at all, confused. 
        Nothing reveals itself to you. This darkness is unlike the others that you have encountered, it is not suffocating. It is pure emptiness. 
        You are unable to move, unable to see, unable to sense anything other than the beat of your own heart. And it will stay that way, forever. You remain asleep.
    """)
    game_over()
elif killcount >= 0 and killcount <= 4 and "Lilith's flower" in pockets:
    lilith_fight()
elif killcount >= 0 and killcount <= 4 and path_choice == "left":
    pause()
    say("""
        \nYou slowly manage to move one leg forward. Then another. Step after step, you slowly make your way to the massive pillars, gaining speed as you go. 
        Before you know it, you are sprinting. You don't know why. You are so close to waking up. As you reach the base of the pillars, your surroundings suddenly disappear. 
        You are in pure, dark, void. You can see nothing. You wave your hands in front of your face to test if you can see anything at all, confused. 
        Your stomach falls as you see your fingers covered in blood. You feel the weight of your mistakes hanging from your neck. Your choices flash before your eyes. 
        You are a killer, but not enough of one. You remain asleep.
    """)
    game_over()
elif killcount >= 0 and killcount <= 4 and path_choice == "right":
    pause()
    say("""
        \nYou slowly manage to move one leg forward. Then another. Step after step, you slowly make your way to the massive pillars, gaining speed as you go. Before you know it, 
        you are sprinting. You don't know why. You are so close to waking up. As you reach the base of the pillars, your surroundings suddenly disappear. You are in pure, dark, 
        void. You can see nothing. You wave your hands in front of your face to test if you can see anything at all, confused. 
        Your hand appears to be fractured and refracted throughout your vision hundreds, thousands, millions of times. Your head hurts. You forget who you are. 
        You forget where you are. Why did you end up here? The splitting headache seems to cave your skull in, crushing your brain. You see yourself, floating in the void, 
        iterated infinite times. Your choices flash before your eyes. You aren't strong enough to be here. You remain asleep.
    """)
    game_over()
elif killcount >= 4:
    lilith_fight()

pause()
print("Conratulations. You finally woke up.")

game_start()
exit()

start()