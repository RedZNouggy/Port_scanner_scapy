#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Entry point."""

import argparse
import sys
from scapy.all import *
from my_colors import infotext, errortext
from scapy_modules import syn_scan

# Parameters
parser = argparse.ArgumentParser(description='')
parser.add_argument('-tip', '--target-ip', action="store", required=True, type=str, help='To specify the ip address that you want to scan')
parser.add_argument('-f', '--input-file', action="store",  required=True, type=str, help='To specify a fie that contains a list of different ports that you want to scan on the specified ip address')
parser.add_argument('-v', '--verbose', action="store_true",  required=False, help='To get more info')
args = parser.parse_args()

def main(target_ip, input_file, verbose):
    '''Does everything
    
    Arguments :
    
        --target-ip --> To specify the ip address that you want to scan
        --input-file --> To specify a fie that contains a list of different ports that you want to scan on the specified ip address
        --verbose --> To get more info
    '''
    
    def is_valid_ipv4(ip) -> bool:
        ''' Check if the given string is a valid IPv4 address.
            Arguments:
                ip (str): The string to check.

                Returns:
                bool: True if the string is a valid IPv4 address, False otherwise.
        '''
        # Regular expression pattern to match IPv4 addresses
        ipv4_pattern = r'^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$'

        # Check if the string matches the IPv4 pattern
        match = re.match(ipv4_pattern, ip)
        if match:
            # Check if each octet is within the valid range (0-255)
            for octet in match.groups():
                if not (0 <= int(octet) <= 255):
                    return False
            return True
        else:
            return False

    def is_valid_port(port):
        return 0 <= port <= 65535

    if is_valid_ipv4(target_ip) is False:
        errortext(f"'{target_ip}' is not a valid IPv4.")
        sys.exit(1) # stop script

    port_list = []
    with open(input_file, 'r', encoding='utf-8') as a_file:
        for line_number, line in enumerate(a_file, start=1):
            line = line.strip()  # Remove trailing newline characters
            if line.isdigit():  # Check if the line contains only digits
                port = int(line)
                if is_valid_port(port):
                    port_list.append(port)  # Append the port to the list
                else:
                    if verbose:
                        warning(f"Warning: Port number {port} in line {line_number} is not a valid port and will be ignored.")
            else:
                if verbose:
                    warning(f"Warning: Line {line_number} '{line}' is not a valid integer and will be ignored.")

    if verbose:
        infotext(f"Starting scan on the IP : {target_ip}")
    
    for single_port in port_list:
        syn_scan(target_ip, single_port, verbose)

if __name__ == "__main__":
    main(args.target_ip, args.input_file, args.verbose)
