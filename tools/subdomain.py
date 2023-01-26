#!/usr/bin/python3

import argparse
import requests
from os import path

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--target", help = "Put a domain")
parser = parser.parse_args()

def main():
    if parser.target:
        if path.exists("subdomain.txt"):
            wordlist = open("subdomain.txt",'r')
            wordlist = wordlist.read().split("\n")

            for subdomain in wordlist:
                url = "https://" + subdomain +"." + parser.target
                try:
                    requests.get(url)
                except requests.ConnectionError:
                    print("(-) Connection Error:" + url) 
                else:
                    print("[+] Subdomain: " + url)
                    
            for subdomain in wordlist:
                url = "http://" + subdomain + "." + parser.target
                try:
                    requests.get(url)
                except requests.ConnectionError:
                    pass
                else: 
                    print("[+] Subdomain: " + url)
                    
            

if _name_ == "_main_":
     try:
         main()
     except KeyboardInterrupt:
         exit()
