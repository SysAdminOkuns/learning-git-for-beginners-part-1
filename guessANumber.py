'''
This is our simple 
guess a number program
'''
# This is a simple line of comment
# Initial the guessable number
number = 10

# An infinite loop
while True:
# User takes a guess
	guess = int(input("Take a guess: "))
# Checking user input against initial guessable number
	if (guess > number):
		print("Too high!")
	elif (guess < number):
		print("Too low!")
	else:
		print("Exactly right!")
		break
