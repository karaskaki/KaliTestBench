#!/usr/bin/env python

import subprocess

subprocess.call("ifconfig ", shell=True)

interfc = input("The interface that needs change > ")
mac_alter = input("New Mac Address: ")
print("[+] Changing Nac Address of: "+interfc + " to " + mac_alter)

subprocess.call("ifconfig " + interfc + " down", shell=True)
subprocess.call("ifconfig " + interfc + " hw ether "+mac_alter, shell=True)
subprocess.call("ifconfig " + interfc + " up", shell=True)

