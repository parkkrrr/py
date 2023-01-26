#
# Find the area and perimeter of rectangle. 
#

length = int(input("Enter the Length: "))
width = int(input("Enter the Width: "))

area = length * width
peri = 2 * (length + width)

print("\nArea of Rectangle is {}".format(area))
print("Perimeter of Rectangle is {}".format(peri))