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

	if guess == 0:
		break
	if guess == answer:
		print("Congrats {}! You have guessed it right.".format(name))
		break		
	else:
		if guess > answer:
			print("Please Guess lower")
		else:
			print("Please Guess higher")
	if times == 5:
		print((" "*50),"# Enter 0 to exit or continue with guessing")
		
	if guess != answer:
		times += 1

if guess == answer and times == 0:
	print("WoW, what a luck.")

elif guess == answer and times <= 10:
	print("Not bad! After {} tries. Well done, {}".format(times, name))
elif guess == answer and times > 10:
	print("OMG! After {} tries. You are very bad at guessing.".format(times))
else:
	print(("-" * 20),"Game Over",("-" * 20))
# elif guess < answer:
	
# elif guess != answer:
# times += 1
	
# if times > 10:
# print("OMG! After {} tries. You are very bad at guessing.".format(times))
# work in progress
		

	