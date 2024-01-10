#! /usr/bin/env python

import scapy.all as scapy

""""
 The communication inside the network is carried out using the MAC address and not the IP address
 MAC address is discovered by ARP that links IPs with MACs. Sends a broadcast message, ARP request, asking who has the X IP.
"""

def scan(ip):
    # Use ARP to ask who has the target IP --> create ARP request
    arp_request = scapy.ARP(pdst=ip)
    # Set destination MAC to broadcast MAC --> destination is set in the ethernet part of the packet
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast= broadcast/arp_request
    print(arp_request_broadcast.summary())

scan("192.168.1.1/24")