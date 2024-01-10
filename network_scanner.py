#! /usr/bin/env python

import scapy.all as scapy

""""
 The communication inside the network is carried out using the MAC address and not the IP address
 MAC address is discovered by ARP that links IPs with MACs. Sends a broadcast message, ARP request, asking who has the X IP.
"""

def scan(ip):
    # Create packets by:    Use ARP to ask who has the target IP
    #                       Set destination MAC to broadcast MAC
    arp_request = scapy.ARP(pdst=ip)
    print(arp_request.summary())

scan("192.168.1.1/24")