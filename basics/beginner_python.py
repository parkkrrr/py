#!/bin/python3

name = "The Great Prakhar"
print("\t\t", name)

print("Lowercase: ", name.lower())
print(name.islower())

print("Uppercase: ", name.upper())
print(name.isupper())

print(name.upper().isupper())

print("Length", len(name))
print("Position 10: ", name[10])

print("Index Value (P): ", name.index('P'))

print("Replace: ", name.replace("Prakhar", "Parker"))


# Working with Numbers 
#

print("\nWorking with Numbers")

num = -5
print(num)
print("Absolute value: ", abs(num))

print("Power: ", pow(4, 6))

print("Max: ", max(4, 6))   # Two parameters
print("Min: ", min(4, 6))   # """""""""""""" 
print("Round: ", round(3.7))

from math import *

print("Floor: ", floor(3.7))           # Chop off the decimal points
print("Ceil: ", ceil(3.7))
print("Squareroot: ", sqrt(36))

