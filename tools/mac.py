#!/usr/bin/env python

import subprocess

interface = input("Interface Name \n> ")
mac = input("Enter the New MAC Address \n> ")

print("*** Changing the MAC Adress of " +interface+ " to " +mac)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", mac])
subprocess.call(["ifconfig", interface, "up"])
subprocess.call("ifconfig")
