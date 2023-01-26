# Write a program to accept the marks of five subject and calculate the average marks.
#
#

eng = float (input('Enter English Marks: '))
maths = float (input('Enter Maths Marks: '))
ip = float (input('Enter I.P. Marks: '))
arts = float (input('Enter Painting Marks: '))
eco = float (input('Enter Economics Marks: '))

total = eng + maths + ip + arts + eco
avg = total / 5

print ('Average Marks is: ', avg)