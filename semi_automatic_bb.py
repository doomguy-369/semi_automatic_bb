#!/usr/bin/env python

import os
import time
import sys


banner = """
                                                                                
               (%&&&&&%#%#%%%%%%%%%%&*******%%%%%%%&%#&&&%%&%&%%%%%%%           
               &&&&&&&&&%@&&@&&&&&&@@*/////&&&&&&&&&&&&%&&&&%%&&&&&&&&&           
              (%%&&&&%&&&&&@%%%&@&&&&&&&&&&&&%&&%&&%&%&&&&&%&&%&%@@&&&&           
               #%%&&&#%%%&&&&&&&%%%&%%&%@@%&%&&&&@@@@@@&@@&&&&&&&&&&&           
                    &#%%&&&&&&&&&&&&%,       %&                                 
                   %%(%%%%%%%&&&&& @((        (                                 
                  &&##%%&&&&&&%%%&   (@ _===_,%                                 
                %&%##%%&&&%%&&                                                  
               (&###%&&&&&&&&%                                                  
              &&%#(%&&&&&&&&%                    SEMI                               
              %%#%%%&&&&&&%&                     AUTOMATIC                               
             &%#&%&%&&%&%&&                      BUG                               
            %&%#%&&%&&&#%&*                      BOUNTY                               
            &%%#&&%&&&%&&&                                                      
            &%%&&&&&&&&&&&                                                      
                                                                                
"""
class bcolors:
    HEADER =    '\033[95m'
    OKBLUE =    '\033[94m'
    OKCYAN =    '\033[96m'
    OKGREEN =   '\033[92m'
    WARNING =   '\033[93m'
    FAIL =      '\033[91m'
    ENDC =      '\033[0m'
    BOLD =      '\033[1m'
    UNDERLINE = '\033[4m'
    ITALIC =    '\033[3m'
    BLINK =     '\033[5m'

class MainMenu:
    def __init__(self):
        print(banner)
        print('[ 1 ] - Add Project')
        print('[ 2 ] - Edit Project')
        print('[ 3 ] - Start Scann')
        print(f'{bcolors.WARNING}[ x ] {bcolors.ENDC}- Exit')
        inp = input('\n[ ? ] Select Option >>> ')

        if inp == '1':
            pass

        if inp == '2':
            pass

        if inp == '3':
            pass

        if inp == 'x':
            print(f'\n{bcolors.OKCYAN}[...] Bye')
            sys.exit()

        else:
            print(f'\n{bcolors.FAIL}[ ! ] Code Error{bcolors.ENDC}')
            time.sleep(2)
            restart = MainMenu()


class UserInput:
    def __init__(self):
        self.project = input("Enter project name: ")
        self.url = input("Enter URL: ")
        self.ip = input("Enter IP address: ")

if __name__ == '__main__':
    try:
        start = MainMenu()
    except KeyboardInterrupt:
        print(f'\n{bcolors.FAIL}[!!!] Keyboard Interrupt')
