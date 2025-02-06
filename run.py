# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

# Python Text RPG
# by Malte M. Boettcher

import cmd # imports command functions
import textwrap # displays text in wraps
import sys # imports system functions
import os # imports operating systems functions
import time # imports time related functions (counter, calender, clock, etc...)
import random # randomizes 

screen_width = 100 # sets output window to full screen 100% width

#### Player Setup ####
class player:
    def __init__(self):
        self.name = ""
        self.hp = 0
        self.mp = 0
        self.status_effects =[] # emty array
myPlayer = player()

#### Title Screen ####
def title_screen_selections():
    option = input("> ")
    if option.lower() == ("play"):
        start_game() # placeholder until written
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("quit"):
        sys.exit() # system function to exit program
    while option.lower() not in ["play", "help", "quit"]: # shows options while player is undecided
        print("Please enter a valid command.")
        option = input("> ")
        if option.lower() == ("play"):
            start_game() # placeholder until written
        elif option.lower() == ("help"):
            help_menu()
        elif option.lower() == ("quit"):
            sys.exit() # system function to exit program

def title_screen():
    os.system("clear")
    print("############################")
    print("# Welcome to the Text RPG! #")
    print("############################")
    print("          - Play -          ")
    print("          - Help -          ")
    print("          - Quit -          ")
    print("   by  Malte M. Boettcher   ")
    title_screen_selections()

def help_menu():
    print("##################################")
    print("            Help Menu            #")
    print("##################################")
    print("- Use up, down, left right to move")
    print("- Type your commands to do them   ")
    print("- Use 'look' to inspect something ")
    print("     Good luck and have fun!      ")
    title_screen_selections()

def start_game():