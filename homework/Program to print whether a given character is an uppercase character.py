#
# Write a program to print whether a given character is an uppercase character or a digit or any other character.
#

charac = input('Enter any character: ')
if charac.isupper() :
    print(charac, 'is uppercase character')
elif charac.islower() :
    print(charac, 'is lowercase character')
else :
    print(charac, 'is a digit maybe :p')