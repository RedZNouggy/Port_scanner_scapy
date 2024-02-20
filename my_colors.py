#!/usr/bin/env python3

from colorama import Fore, Style

# Info message
def infotext(msg) -> str:
    '''Display informational message on console in blue

    Arguments:

    msg -- text to be printed
    '''
    print(f"{Fore.BLUE}[i] {msg} {Style.RESET_ALL}")
# Error message
def errortext(msg) -> str:
    '''Display success message on console in green

    Arguments:

    msg -- text to be printed
    '''
    print(f"{Fore.RED}[-] {msg} {Style.RESET_ALL}")
# Success message
def successtext(msg) -> str:
    '''Display success message on console in green

    Arguments:

    msg -- text to be printed
    '''
    print(f"{Fore.GREEN}[+] {msg} {Style.RESET_ALL}")
# Warning message
def warntext(msg) -> str:
    '''Display warning message on console in yellow

    Arguments:

    msg -- text to be printed
    '''
    print(f"{Fore.YELLOW}[+] {msg} {Style.RESET_ALL}")
