#! /usr/bin/env python

import subprocess
import optparse

"""""
MAC: Media Access Control --> Permanent Physical Unique
Packets flow from source MAC to destination MAC

To change:  ifconfig eth0 down
            ifconfig eth0 hw ether 00:11:22:33:44:55
            ifconfig eth0 up

"""""

def get_arguments():
    parser = optparse.OptionParser()
    # OptionParser (class in optparse module) deprecated in favor of argparse module
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    (options, arguments) = parser.parse_args()
    # returns to sets of information: values (what the user has introduced) and arguments (--interface, --mac) 
    if not options.interface:
        parser.error("Specify an interfeface")
    elif not options.new_mac:
        parser.error("Specify a new MAC")
    return options

def change_mac(interface, new_mac):
    print("Changing MAC address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

options = get_arguments()
change_mac (options.interface, options.new_mac)