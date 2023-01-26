name = input("Enter your name: ")
age = int(input("Enter your age: "))

if 18 <= age <= 30:
	print("Hello {}, You are welcome to the holiday.".format(name))
else:
	print("Sorry {}, You must be over 18 and under. 31\nI'm sorry, our holidays are only for cool people.".format(name))

print(input("You can exit!"))