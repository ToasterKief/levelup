#!/usr/bin/python3

#Modules
import os
import os.path 
import sys
import time
import json
from testfunction import test_function
 
#from lib.levelup_classes import *
#from lib.levelup_menus import *

#functions
"""
The purpose of the 'levelup_main()' function is to handle the actual game's engine and will import various modules to handle the interactive elements of the program as well as some of the underlying mechanics.
"""

def levelup_main(load_session):
    if load_session == False: 
        os.system("clear")
        time.sleep(0.5)
        print("levelup_main function executed with the intention of initializing the new user script.\n")
        time.sleep(1.0)
        test_function()
    
    elif load_session == True: 
        os.system("clear")
        time.sleep(0.5)
        print("levelup_main function executed with the intention of initializing the script that reads json save file\n")
        time.sleep(1.0)
        test_function()
        

