print("""You enter a dark room with two doors.
Do you go through door #1 or door #2? or door #3""")
door = input("> ")
if door == "1":
    print("There'sa giant bear here eating a cheese cake.")
    print("What doyou do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")
    print("3. shoot the bear with your gun")
    bear = input("> ")
    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    elif brear =="3":
        print("Sorry you forget to reload. Good job!")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")

elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")
    insanity = input("> ")
    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")
elif door =="3":
    print("There is nothing behind this boord, and you walk back home")
    secretvictory = input(">")
    if secretvictory == "1":
        print("Everyting is a lie, you are fake, everything is not real this is a python program")
else:
    print("You stumble around and fall on a knife and die. Good job!")
