#!/bin/python3

def say_hi():
	print("Hello User")

say_hi()

# Passing the Parameters

def say_hello(name, age):
	print("Hello " + name + ", you are " + age)
	
say_hello("Prakhar", "18")
say_hello("Parker", "16")

# Using the return statement

def cube(num):
	return num*num*num

result = cube(4)
print(result)

# Using with if statement

def max_num(num1, num2, num3):
	if num1 >=num2 and num1 >= num3:
		return num1
	elif num2 >= num1 and num2 >= num3:
		return num2
	else: 
		return num3
		
print(max_num(300, 412, 50))

