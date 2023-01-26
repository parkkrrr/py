#
# To take a value from the user and print the square of it until it is more than 120.
#

x = float(input("Enter a value: "))
a = 0
while a == 0:
    s = x ** 2
    if s <= 120:
        print("{} square is {} ".format(x,s))
        x += 1
    else:
        break
