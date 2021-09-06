from sys import argv

script, user_name, suffix = argv
prompt = '>_< '

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)
print("Where do you live %s " %(user_name))
lives = input(prompt)
print("What kind of computer do you have?" )
computer = input(prompt)
print("""
Alright you said %r about liking me
You live in %r, not sure where that is
and you have a %r computer, nice
"""%(likes,  lives, computer))
