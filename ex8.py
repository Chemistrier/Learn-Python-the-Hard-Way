formatter = "{} {} {} {}"#create a sequence with four slots

print(formatter.format(1, 2, 3, 4))# input 4 integers
print(formatter.format("one", "two", "three", "four"))#input 4 words
print(formatter.format(True, False, False, True))#input 4 boolean value
print(formatter.format(formatter, formatter, formatter, formatter))#input 4 slots sequence in side every slots, which create 16 slots
print(formatter.format(
    "I am the bone of my sword",
    "Unknown to death",
    "nor to life",
    "heart is glass"
))#input 4 lines of string 
