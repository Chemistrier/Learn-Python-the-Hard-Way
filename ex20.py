from sys import argv #import argv

script, input_file = argv #script and input_file is argv
def print_all(f): #define print_all
    print(f.read())#print things in the file

def rewind(f):#define rewind
    f.seek(0)#use seek method
def print_a_line(line_count, f):#define print a line
    print(line_count, f.readline())#print line conut and file content

current_file = open(input_file)#current_file open input_file

print("First let's print the whole file:\n")#print

print_all(current_file)#call print_all, function used

print("Now let's rewind, kind of like a tape.")#print
rewind(current_file)#call rewind function used

print("Let's print three lines:")#print

current_line = 1#currentline is 1
print_a_line(current_line, current_file)#call  print_a_line with current_file and line current_line is 1. function used

current_line += 1# currentline +1
print_a_line(current_line, current_file)#call  print_a_line with current_file and line again current_line is 2. function used

current_line +=  1# currentline +1
print_a_line(current_line, current_file)#call  print_a_line with current_file and line again current_line is 3. function used

#pydoc file.seek:
'''
Argument offset is a byte count.  Optional argument whence defaults to
    0 (offset from start of file, offset should be >= 0); other values are 1
    (move relative to current position, positive or negative), and 2 (move
    relative to end of file, usually negative, although many platforms allow
    seeking beyond the end of a file).  If the file is opened in text mode,
    only offsets returned by tell() are legal.  Use of other offsets causes
    undefined behavior.
    Note that not all file objects are seekable.
'''
