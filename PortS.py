"""
WHAT IS A PORT SCANNER?
Scenario: a server hosts different services on different ports i.e http -> 80, SSH -> 22, FTP -> 21
A port scanner allows an attacker to find open ports on the server.
nmap is the industry goto/standard... but let's make our own for fun!

Port scanner needs to:
1. select target
2. make requests to every port
3. return open ports

Expand:
1. List protoles used on each port
2. Make use of threading to make application faster
"""
import sys

import pyfiglet
import os
import socket
from datetime import datetime

"""Banner to look nice and like a hacker from the 80s"""
ascii_banner = pyfiglet.figlet_format("Port Scanner")
print(ascii_banner)

"""Get the target ip address to scan"""
target = input("Target IP: ")

"""Look cool..."""
print("_" * 50)
print("\nScanning Target: " + target)
print("Scan started at: " + str(datetime.now()))
print("_" * 50)

"""The actual program"""
try:
    for port in range(1, 65535):
        #scan every port on the target ip
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)

        #return every port
        result = s.connect_ex((target, port))
        if result == 0:
            print("[*] Port {} is open".format(port))
        s.close()
except KeyboardInterrupt:
    print("Exiting")
    sys.exit()

except socket.error:
    print("Host not responding")
    sys.exit()














