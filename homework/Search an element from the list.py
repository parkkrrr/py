# WAP to search an element from the list


L = eval (input("Enter the elements:"))
n = len (L)
flag = 1

s = int(input("Enter the element to be searched:"))
for i in range(0,n-1):
	if(L [i] == s):
		flag = 1
		break;
	else:
		flag = 0
		
if flag == 1:
	print("Element found")
else:
	print("Element not found")
	
print(input())

