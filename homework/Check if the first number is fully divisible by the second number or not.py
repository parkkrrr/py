#
# Write a program that accepts two numbers and check if th first number is fully divisible by the second number or not.
#

n1 = float(input("Enter a Number: "))
n2 = float(input("Enter the Number: "))

if n1 % n2 == 0:
	print("{} is fully divisible by the second number".format(n1))
else:
	print("{} is not fully divisible by the second number".format(n1))