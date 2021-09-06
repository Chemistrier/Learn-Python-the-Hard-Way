#This is a variable
cars = 100
#This is a variable
space_in_a_car = 4.0
#This is a variable
drivers = 30
#This is a variable
passengers = 90
#This is a variable

cars_not_driven = cars - drivers
#This is a variable

cars_driven = drivers
#This is a variable

carpool_capacity = cars_driven * space_in_a_car
#This is a variable

average_passengers_per_car = passengers / cars_driven
#This is a variable

rickweight = 10000

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
print("Rick's car is ",rickweight,"kg heavy")
#it is neccessary because the space_in_a_car can't be simply an integer
