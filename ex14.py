from sys import argv

script, user_name, suffix = argv
prompt = '>_< '

print("Hi %s, I'm  the %s script. "%(user_name, suffix, script))
print("I'd like to ask you a few questions")
print("Do you like me %s?. " %(user_name, suffix)
likes = input(prompt)
print("Where do you live %s" %(user_name, suffix))
lives = input(prompt)
print("What kind of computer do you have?" )
computer = input(prompt)
print("""
Alright you said %r about liking me
You live in %r, not sure where that is
and you have a %r computer, nice
"""%(likes,  lives, computer))