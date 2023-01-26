#
# Write a program that accepts the age and print if one is eligible to vote or not.
#

eligibility = int(18)
age = int(input('Enter your AGE: '))

if age < eligibility:
    print('You are not eligible to vote') 

if age >= eligibility:
    print('You are eligible to vote')

