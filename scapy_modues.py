#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Entry point."""

from scapy.all import *
from my_colors import infotext, successtext, errortext

# output format # TODO make prettier 
def print_ports(port, state):
	infotext("%s | %s" % (port, state))

def syn_scan(target_ip, port, verb):
    '''Does a syn scan on the specified target ip and port
    
    Arguments :
    
        --target-ip --> To specify the ip address that you want to scan
        --port --> To specify a port that you want to scan on the specified ip address
        --verb --> To get more info
    '''
    # Send SYN packet to the specified port
    response = sr1(IP(dst=target_ip)/TCP(dport=port, flags="S"), timeout=2, verbose=verb)
    
    # Check if a response was received
    if response is not None:
        # Check if the response has a TCP layer and the SYN-ACK flag is set
        if response.haslayer(TCP) and response[TCP].flags & 0x12:
            if verb:
                successtext(f"Port {port} is open on {target_ip}")
        else:
            if verb:
                errortext(f"Port {port} is closed on {target_ip}")
    else:
        if verb:
            errortext(f"No response received for port {port} on {target_ip}")

