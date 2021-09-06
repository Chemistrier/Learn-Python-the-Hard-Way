
numbers = []
def thefunction(i, j, z):
    while i < j:
        print(f"At the top i is {i}")
        numbers.append(i)
        i=i+z
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")
def anotherfunction(i,j,z):
    for i in range(i,j):
        print(f"At the top i is {i}")
        numbers.append(i)
        i=i+z
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")
thefunction(1,7,2)
print("The numbers: ")
for num in numbers:
    print(num)
#no you don't need to add increment, the for loop will use the same increment
