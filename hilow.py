low = 1
high = 1000
name = input("Enter your name: ")
print("Hello {}, Think of a number between {} to {}: ".format(name,low, high))
print("If you want to quit the game in between just type 'quit' ")
input("\nPress Enter to start")		# This will just show the message "Press Enter"

guesses = 1
while True: 				# while guess != answer:
	guess = low + (high - low) // 2
	high_low = input("My guess is {}. Should I guess higher or lower? Enter h or l, or c if my guess was correct.\n".format(guess)).casefold()

	if high_low == 'quit':
		print("-"*20,"Game Over","-"*20)
		break
		
	if high_low == "h":
		# Guess higher. The low end of the range becomes 1 greater than the guess.
		low = guess + 1
	elif high_low == "l":
		# Guess lower. The high end of the range becomes one less than the guess.
		high = guess - 1
	elif high_low == "c":
		print("I got it in {} guesses!".format(guesses))
		break
	else:
		print("Enter h, l or c")
	
	guesses += 1 
	
	
	
	