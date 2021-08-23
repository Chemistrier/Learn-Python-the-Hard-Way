from sys import argv #import argv from sys

script, filename = argv # assign two arguments

txt = open(filename) # open the file that has the filename and store it into txt
print("Here's your file %r: "%(filename)) #print out the filename
print(txt.read())#read the text stored in txt
txt.close()
print("type filename again:")#ask the user to type the filename again
file_again = input("> ")#take the filename again
txt_again = open(file_again)#ppen the file again using file_again
print(txt_again.read())#print out the things stored in txt_again
txt_again.close()
#the content in the file will not print twice
#using input() will ask the filename after the program start running, but using arguments will use the inputted value directly, input() will be convenient if you want to tell the user to input the way you want and arguments is simply faster to running
