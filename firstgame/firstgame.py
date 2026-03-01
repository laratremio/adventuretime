name = input("Type your name: ")
print("Welcome!", name, "to this adventure..")

answer = input("You open your eyes, you're confused. Your vision slowly returns and you get up. Two doors are in front of you. Left or right door?" ).lower()

if answer == "left":
    answer ==input("You enter a room that looks like a normal pool Expect it is quiet, too quiet... there is a slide and an emergency exit door. Type slide to take the slide, type door to go through the exit door: ")
elif answer == "right":
    print()
else: print('Not a valid option. You feel a heat. You are dead')
