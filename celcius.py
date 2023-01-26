#
#
#

def celcius(x):
    return(x-32)*5/9

for x in range(0,101,5):
    print("{:>3} F | {:6.2f} C".format(x,celcius(x)))
