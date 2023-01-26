#
# Write a program to display a menu for calculating area of circle or perimeter of the circle.
#
pi = 3.14159
r = float(input('Input Radius: '))
aoc = pi * r * r
perimeter = 2 * pi * r

print ('Menu-\n1. Area of Circle\n2. Perimeter of the Circle')
x = int(input("Enter the number | What you want to calculate? '1' or '2'  "))

if x == 1:
    print('Area of Circle: ', aoc)

elif x == 2:
    print ('Perimeter of the Circle: ', perimeter)

else:
    print('Invalid Input! Please try again.')