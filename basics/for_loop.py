#!/bin/python3

for letter in "Giraffe Academy":
    print(letter)
    
friends = ["Parker", "Andy", "Choli"]
for friend in friends:
    print(friend)

for index in range(len(friends)):
    print(friends[index])

for index in range(5):
    if index == 0:
        print("First Iteration")
    else:
        print("Not First")

def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

print(raise_to_power(3, 4))
