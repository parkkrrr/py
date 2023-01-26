#
#Guessing Game

import random

highest = 20

name = input("Enter your name: ")
print("Hello {}, Thank you for trying my python project\nI'll promise, you will regret\nLet's begin!".format(name))

answer = random.randint(1, highest)
print("Please guess the number between 1 to {}: ".format(highest))
guess = int(input())

print(answer)

if guess == answer:
 	print("Congrats {}! You have guessed it right.".format(name))
else:
	if guess > answer:
		print("Please Guess lower")
	else:
		print("Please Guess higher")

	guess = int(input())
	
	if guess == answer:
		print("Well Done! {}".format(name))
	else:
		print("You have not guessed correctly,{}".format(name))
