people = 20
cats = 30
dogs = 15
if people < cats:
    print("Too many cats! The world is doomed!")
if people > cats:
    print("Not many cats! The world is saved!")
if people < dogs:
    print("The world is drooled on!")
if people > dogs:
    print("The world is dry!")
dogs += 5
if people >= dogs:
    print("People are greater than or equal to dogs.")
if people <= dogs:
    print("People are less than or equal to dogs.")
if people == dogs:
    print("People are dogs.")
if people != dogs:
    print("People are not dogs")
#if the statement after if is true then it would do the command under it
#the command is only for that if statement, so it need to be isolate from rest of the code
#it would cause error
#I put !=
# the result of whether human are dogs or cats will change according to  the value that is being set on people cats and dogs 
