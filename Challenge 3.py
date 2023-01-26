#!/usr/bin/python3

print("Please choose your options from the list below:")
print("1. Learn Python ")
print("2. Learn Java")
print("3. Go Swimming")
print("4. Have dinner")
print("5. Go to bed")
print("0. Exit")

while True:

	input_ = int(input("Please select an option: "))

	if input_ == 1:
		print("Learn Python")
	elif input_ == 2:
		print("2. Learn Java")
	elif input_ == 3:
		print("3. Go Swimming")
	elif input_ == 4:
		print("4. Have dinner")
	elif input_ == 5:
		print("5. Go to bed")
	elif input_ == 0:
		break
	else:
		print("Please Select from 0-5.\n ")
	