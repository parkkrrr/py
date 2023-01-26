#
# Write a program that reads two number and an arithmetic operator and displays the computer result.
#

num1 = float (input('Enter first number: '))
ap = input ('Enter operator: ')
num2 = float (input('Enter second number: '))

result = 0
if ap == '+':
    result = num1 + num2

elif ap == '-':
    result = num1 - num2

elif ap == '*':
    result = num1 * num2

elif ap == '/':
    result = num1 / num2

elif ap == '%':
    result = num1 % num2

elif ap == '**':
    result = num1 ** num2

else :
    print('Invalid operator')

print (num1,ap,num2, '=', result)