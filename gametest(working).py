#		if guess == answer:
#			print("Well Done! {}".format(name))
#		else:
#			print("You have not guessed correctly,{}".format#(name))
#	if guess.casefold() == "quit":
#	break

#
#Guessing Game

import random

highest = 20

name = input("Enter your name: ")
print("Hello {}, Thank you for trying my python project\nI'll promise, you will regret after this.\nLet's begin!".format(name))

answer = random.randint(1, highest)
times = 0
print("Please guess the number between 1 to {}: ".format(highest))
while True:
	guess = int(input())

	if guess > answer:
		    print("Please Guess lower")
	elif guess < answer:
		print("Please Guess higher")
	else:
		print("Congrats {}! You have guessed it right.".format(name))
		break
    
	if guess != answer:
		times += 1
	
if times > 10:
	print("OMG! After {} tries. You are very bad at guessing.".format(times))
else:
	print("After {} tries! Not bad.".format(times))
		

	