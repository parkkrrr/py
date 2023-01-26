#
# Check whether given number is positive or negative
# 

n = float(input("Enter a Number: "))

if n > 0:
    print("{} is a Positive Number".format(n))
elif n < 0:
    print("{} is a Negative Number".format(n))
else:
    print("{} is neither Positive nor Negative Number".format(n))
