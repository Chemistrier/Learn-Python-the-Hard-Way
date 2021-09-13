ten_things = "Apples Oranges Crows Telephone Light Sugar"
print("Wait there are not 10 things in that list. Let's fix that.")
stuff = ten_things.split(' ')#split(ten_things) split ten things when a ' ' occurs
more_stuff = ["Day", "Night", "Song", "Frisbee",
              "Corn", "Banana", "Girl", "Boy"]
while len(stuff) != 10:
    next_one = more_stuff.pop()#pop(more_stuff) Call pop on more_stuff.
    print("Adding: ", next_one)
    stuff.append(next_one)#append(next_one) add next_one to the end of stuff
    print(f"There are {len(stuff)} items now.")
print("There we go: ", stuff)
print("Let's do some things with stuff.")
print(stuff[1])
print(stuff[-1]) # whoa! fancy print(stuff.pop())
print(' '.join(stuff)) # what? cool! print('#'.join(stuff[3:5])) # super stellar! join(stuff) #join everything together with ' '
#i read, this is same with java
'''
Classes provide a means of bundling data and functionality together.
 Creating a new class creates a new type of object, allowing new instances of that type to be made.
 Each class instance can have attributes attached to it for maintaining its state.
 Class instances can also have methods (defined by its class) for modifying its state.
'''
#i get it, I learn java before
#names, fruits, phone numbers, home addresses, score, school list, price, class list, company names, type of language
