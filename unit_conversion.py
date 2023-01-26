#!/usr/bin/python3

print("Convert Kg to Lbs or vice versa.")

try:
    weight = int(input("Enter the Weight: "))
    unit =  input("(K)g or (L)bs: ")

    if unit.upper() == "L":
        converted = weight * 0.45
        print(f"You are {converted} Kg")
    if unit.upper() == "K":
        converted = weight // 0.45
        print(f" You are {converted} Lbs")
except:
    print("Something went wrong")
