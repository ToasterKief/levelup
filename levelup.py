#!/usr/bin/python3 
"""
Below are the necessary modules to run the levelup program. The 'os' module is important because it gives us functionality on an operating system level. The time module is quite useful when it comes to menus and pacing the script. Below those we'll find modules that make up the content of the program.
"""
import sys
import os
import time
from levelup_menus import * 
from levelup_main import levelup_main
from testfunction import test_function
# Main function



def main():
    while True:
        os.system('clear')
        time.sleep(.5)
        welcome_levelup()
        os.system("clear")
        time.sleep(.5)
        welcome_menu()
        savefile_input = str(input("Please enter a choice from the options given to you => "))
        if savefile_input == "1":
            """
            os.system("clear")
            print("Option '1' is functional\n")
            time.sleep(2.0)
            test_function()
            """
            levelup_main(load_session= False)
            
        
        elif savefile_input == "2":
            """
            os.system("clear")
            print("Option '2' is functional\n")
            time.sleep(2.0)
            test_function()
            """
            levelup_main(load_session = True)
            
            
        elif savefile_input == "99":
            os.system("clear")
            time.sleep(0.1)
            print("Now exiting the program..\n")
            time.sleep(0.6)
            print("Hope you enjoyed it!\n")
            time.sleep(0.5)
            sys.exit(0)
            
        
if __name__ == "__main__":
    main()

            
        
        
