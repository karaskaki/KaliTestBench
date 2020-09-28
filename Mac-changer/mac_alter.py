#!/usr/bin/env python3

import subprocess
import optparse


# subprocess.call("ifconfig ", shell=True)

def get_args():
    bullet = optparse.OptionParser()
    bullet.add_option("-i", "--interface", dest="interfc", help="Interface of which the MAC Address will change")
    bullet.add_option("-m", "--mac", dest="mac_alter", help="The New MAC Address you want to set")
    return bullet.parse_args()
# parser.error("[-] Please specify mac address/ interface.  ")


def mac_changer(interfc, mac_alter):
    print("\n [+] Updating the MAC Address of: " + interfc + " to " + mac_alter)
    subprocess.call(["ifconfig", interfc, "down"])
    subprocess.call(["ifconfig", interfc, "hw", "ether", mac_alter])
    subprocess.call(["ifconfig", interfc, "up"])
    print(" ")
    subprocess.call(["ifconfig", interfc])


# args has -i, --i and container contains the value of interfc and mac.

x = 0
(container, args) = get_args()
if not container.interfc:
    interfc = input("The interface that needs change > ")
    x = 1
elif not container.mac_alter:
    mac_alter = input("New Mac Address: ")
    x = 2
else:
    interfc = container.interfc
    mac_alter = container.mac_alter
if x==1:
    mac_alter=container.mac_alter
if x==2:
    interfc=container.interfc
mac_changer(interfc, mac_alter)


