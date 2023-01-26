#!/usr/bin/python3

message = input("Enter the message you want to reverse: ")
reverse = (message [::-1])

print(reverse)
after = ""

i = len(message) -1

while i >= 0:
    after += message[i]
    i -= 1

print(after)
agree = input("Do you want to check the both conditions. Yes/No-  ")

if "y" in agree.casefold():
    print("Both are same")

if reverse != after:
    print("Something is Different ")
    print(after, "\n", reverse)
