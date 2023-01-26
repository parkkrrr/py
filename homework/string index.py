#
#
#

while True:
    n1 = input("Enter a Value: ")
    x = int(input())
    if len(n1)> x:
        print("String:{}\nIndex:{}\nOutput:{}".format(n1,x,n1[x]))
    else:
        print("Index is out of range")
