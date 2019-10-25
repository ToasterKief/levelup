#!/usr/bin/python3
"""
This entire module is necessary to render the terminal based prompts for the various in game menus. It typically doesn't handle user input or the actual menu navigation, but instead the scripting and design of those menus.
"""
#Module imports here
import os
import sys
import time

# Menu functions 



""" 
This menu will eventually become an ASCII art banner for the program. It's a purely aesthetic feature and won't likely get any attention until much later in the project.
"""
def welcome_levelup():
	print("This menu is still currently under development,\n")
	time.sleep(2)
	print("However you may still wait 3 seconds for the main program to start..\n")
	time.sleep(3)
	
"""
"""	
	
def welcome_menu():
	print("=>=>=>=>=>=>=>=>|| Level Up Terminal Based Gamification\n")
	time.sleep(1.5)
	print("\n" * 2)
	print("A project by Toasterkief\n")
	time.sleep(1.0)
	os.system("clear")
	time.sleep(0.2)
	print("Create a new save file or load a previous session?\n")
	time.sleep(0.2)
	print("[1] Start a new save file.\n")
	time.sleep(0.1)
	print("[2] Load a previous session.\n")
	time.sleep(0.1)
	print("[99] Exit the program.\n")
	time.sleep(0.1)
	
	
