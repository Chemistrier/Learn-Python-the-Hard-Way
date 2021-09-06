people = 30
cars = 40
trucks = 15
if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.")
if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")
if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")
if cars > people or trucks < cars:
    print("Alright, let's just take the trucks.")

#else if mean when the statement after if is wrong, then it will go to else if this is true, when everything doesn't pass through else if or if, then it would go to else and execute the command
#if i switch people and cars's number, then I will get we should not take cars
#testing each boolean expression, and whether it would be true and the command under it will execute 
