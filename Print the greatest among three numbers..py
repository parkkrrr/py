#
# To print the greatest among three numbers.
#

a = float(input("Enter a value: "))
b = float(input("Enter the value: "))
c = float(input("Enter the value: "))

if a > b and a > c:
    print("{} is the greatest".format(a))
elif b > a and b > c:
    print("{} is the greatest".format(b))
else:
    print("{} is the greatest".format(c))