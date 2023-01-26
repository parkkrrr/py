#!/bin/python3

import sys
import time

# text with extra chars at the start and at the end
data = ["", "b","u","f","f","e","r","i","n","g", ""]

# display with one upper char

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

    time.sleep(1)