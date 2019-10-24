#!/usr/bin/python3 

# Module imports go down here.
import os
import time
# from levelup_menus import welcome_levelup
from lib/levelup_menus import welcome_menu 
# from levelup_main import  levelup_main

# Main function


def main():
    while True:
        os.system('clear')
        time.sleep(.5)
        welcome_levelup()
        os.system("clear")
        time.sleep(.5)
        welcome_menu()
        welcome_choice = str(input("Enter the path to a previous save file or press type 'NEW' => \n"))
        if welcome_choice == "new" or welcome_choice == "NEW":
            levelup_main()
        
        else:
            levelup_main(welcome_choice)
        
if __name__ == "__main__":
    main()

            
        
        
