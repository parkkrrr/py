#
# To find the sum of odd and even numbers from 1 to n.
#

n = int(input("Enter a Number: "))
even = 0
odd = 0
for i in range(1, n+1):
    if i % 2 == 0:
        even += i
    else:
        odd += i

print("Sum of Even no. from 1 to {} = {}".format(n, even))

print("Sum of odd no. from 1 to {} = {}".format(n, odd))
