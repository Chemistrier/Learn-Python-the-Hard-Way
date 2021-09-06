print("Do you want to play this game?1 for yes 2 for no")
ans = input(">")
if ans == "1":
    print("Great you want to play, what door do you want to open")
    ans2 = input(">")
    if ans2 == " ":
        print("Nice there is no door to open")
        print("This is a boring game, do you want to leave")
        ans3 = input("> ")
        if ans3 == "1":
            print("Death is the only way to leave")
        elif ans3 == "2":
            print("Then you are forever trapped")
    else:
        print("There is a monster behind the door, you are dead")
elif ans == "2":
    print("Then why are you even here, you are dead now")
else:
    print("Great instinct, you can leave safely")
