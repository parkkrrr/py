#!/bin/python3

import socket
import termcolor


def scan(targets, ports):
	print("\n[*] Scanning IP Address of {}".format(targets))
	for port in range(1, ports):
		scan_port(targets, port)

def scan_port(ipaddress, port):
	try:
		sock = socket.socket()
		sock.connect((ipaddress, port))
		print("[+] Port {} is Open".format(port))
		sock.close()
	except: 
		#print("[-] Port {} is Close".format(port))
		pass

targets = input("[*] Enter Targets to Scan: ")
ports = int(input("[*] Enter How Many Ports You Want to Scan: "))

if ',' in targets:
	print(termcolor.colored(("[*] Scanning Multiple Targets"), 'red'))
	for ip_addr in targets.split(','):
		scan(ip_addr.strip(' '), ports)
else:
	scan(targets, ports)