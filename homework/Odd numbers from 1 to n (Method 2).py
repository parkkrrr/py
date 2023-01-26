# Develop a series of odd numbers from 1 to n

start, end = 1, int(input("Enter a value: "))
for i in range(1,end):
	if i % 2 != 0:
		print(i)

print(input())
