name = input("Type your name: ")
print("Welcome!", name, "to this adventure..")

answer = input("You open your eyes, you're confused. Your vision slowly returns and you get up. Two doors are in front of you. Left or right door?" ).lower()

if answer == "left":
    answer ==input("You enter a room that looks like a normal pool Expect it is quiet, too quiet... there is a slide and an emergency exit door. Type slide to take the slide, type door to go through the exit door: ")

    if answer == "slide":
        print("The slide keep going, and going, and going... you fall into a big open pool. It is pitch black. You hear an eerie muffled sound. Type stay to keep quiet. Type swim to swim away from the sound")
    elif answer == "door":
        print("The door leads to an open field. There is one house. You go to the door. Type knock or enter." )
    else:  print('Not a valid option. You feel a heat. You are dead' )


elif answer == "right":
    answer = input("It seems like this door leads back home. You walk through it. Something feels off. It is the street you grew up in, only it is too quiet and empty. Type home to walk to your house, type help to scream for help.")
else: print('Not a valid option. You feel a heat. You are dead' )
