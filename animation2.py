#!/bin/python3

import sys
import time

data = ["P","r","a","k","h","a","r"," ","i","s"," ","G","r","e","a","t"]

# display with one upper char

def animation():
	for x in range(len(data)):
	    # remeber lower char
	    old = data[x]

	    # replace with upper char
	    data[x] = old.upper()

	    # create full text
	    text = "".join(data)

	    # display full text
	    sys.stdout.write("\r")
	    sys.stdout.write(text)
	    sys.stdout.flush()

	    # put back lower char
	    data[x] = old

	    time.sleep(0.2)
	    
while True:
	animation()

# display without upper chars at the end 

text = "".join(data)

sys.stdout.write("\r")
sys.stdout.write(text)
sys.stdout.flush()
