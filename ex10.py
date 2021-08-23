tabby_cat = " \tI'm tabbed in"
persian_cat = "I'm split\non a line"
backslash_cat = "I'm \\ a \\ cat"

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
print("I am 6'2\" tall \a \b \f I don't know \\ what this \v is  ")
#you can avoid " would end the line early with  ''' instead of """
# %r shows the way the input is typed in, but %s would add '' or () to the input
