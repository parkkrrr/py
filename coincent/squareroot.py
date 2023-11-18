import math

num_list = input("Enter comma-separated list of numbers: ").split(",")

sqrt_list = [math.sqrt(float(num)) for num in num_list]

print(sqrt_list)
