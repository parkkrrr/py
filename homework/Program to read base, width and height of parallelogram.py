#
# Write a program to read base, width and height of parallelogram and calculate its area and perimeter.
#

base = int(input('Enter the Base: '))
width = int(input('Enter the Width: '))
height = int(input('Enter the Height: '))

area = base * height
perimeter = 2 * base + 2 * width

print ('Area of Parallelogram is: ', area)
print ('Perimeter of Parallelogram is: ', perimeter)
