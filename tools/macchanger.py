#!/usr/bin/env python

# Date created: 27 May 2021
# Author: Prakhar 

import subprocess
import optparse as op								                               

def get_arguments():
    parser = op.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC Address")
    parser.add_option("-m", "--mac", dest="mac", help="New MAC Address")
    (options, arguments) = parser.parse_args()
    
    if not options.interface:
    	# this code block is for handling the errors
    	parser.error("[-] Please specify an interface, use --help for more info.")
    elif not options.mac:
    	# this code block is for handling the errors
        parser.error("[-] Please specify a MAC Address, use --help for more info.")
    return options

def change_mac(interface, mac):
    print("\n[+] Changing the MAC Address for {} to {}".format(interface, mac))				

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", mac])
    subprocess.call(["ifconfig", interface, "up"])

options = get_arguments()

change_mac(options.interface, options.mac)