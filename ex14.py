from sys import argv
script=argv
user_name=argv
promt='>'
print(f"Hii {user_name}, I'm the {script} script.")
print("I would like to ask you some question")
print(f"Do you like me {user_name}?")
likes = input()
print(f"Where do you live {user_name}")
lives =input()
print("What kind of computer do yu have")
computer = input()
print(f"""
Alright, so you said {likes} about liking me
you live in {lives}. Not sure where that is
And you have a {computer} Computer. Nice """ )