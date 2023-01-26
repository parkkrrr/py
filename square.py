a = 0
while a == 0:
    x = float(input("Enter a Number: "))
    s = (x ** 2)
    if s <= 120:
        print("{} square is {}".format(x,s))
    else:
        break