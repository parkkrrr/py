#
"""
Write a program to input percentage marks of a student and find the grades as per following criteria:
Marks								Grade
>=90								A
75-90								B
60-75								C
Below 60							D
"""
#
marks1 = int(input("Enter your marks: "))
marks2 = int(input("Enter your marks: "))
marks3 = int(input("Enter your marks: "))
marks4 = int(input("Enter your marks: "))
marks5 = int(input("Enter your marks: "))

total = marks1 + marks2 + marks3 + marks4 + marks5
avg = total / 5

if avg >= 90 and avg <= 100:
    print ('Grade A')

elif avg >= 75 and avg <=90:
    print ('Grade B')

elif avg >= 60 and avg <= 75:
    print ('Grade C')

elif avg >= 0 and avg <= 60:
    print ('Grade D')

else :
    print("Invalid Input")