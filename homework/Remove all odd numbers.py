#
# WAP to remove all odd numbers from the given list.
#

l=[2,7,12,5,10,15,23]

for i in l:
        if i % 2 != 0:
            l.remove(i)
print (l)

print(input())
