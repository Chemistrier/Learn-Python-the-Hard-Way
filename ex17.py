from sys import argv
from os.path import exists
import Module

script, from_file, to_file = argv

print("Copying from %s to %s" %(from_file, to_file))

in_file = open(from_file)
indata = in_file.read()

print("The file is %d bytes %d bytes long")

#print("Does the output file exists? %r"%(exists(to_file)))
#print("Ready, hit RETURN to continue, CTRL-C to abort.")
#input()

out_file = open(to_file, 'w')
out_file.write(indata)
print("All Right, all done")
out_file.close()
in_file.close()
#i will remove through comment so you know I type all this
#how long can you make: in_file = open(from_file)
#indata = in_file.read()
#out_file = open(to_file, 'w')
#out_file.write(indata)
#man cat
#you can only open certain amount of file at once, so you need to close files 
