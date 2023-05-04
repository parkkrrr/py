import math

# get list of numbers from user
num_list = input("Enter comma-separated list of numbers: ").split(",")

# calculate square root of each number and store in another list
sqrt_list = [math.sqrt(float(num)) for num in num_list]

# print the square root list
print(sqrt_list)
