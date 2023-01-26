#
# Write a program that accepts two numbers and check if the first number is fully divisible by second number or not.
#

fn = int(input('Enter First Number: '))
sn = int(input('Enter Second Number: '))

if fn % sn == 0:
    print (fn, 'is fully divisible by' ,sn)
else:
    print (fn, 'is not fully divisible by',sn)
