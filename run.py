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
        self.location = "start" # sets location maybe use for case files
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

#### GAME FUNCTIONALITY ####
def start_game():


#### MAP ####

# Player starts at b2
# ----------------
# |a1|a2|a3|a4|a5|
# ----------------
# |b1|b2|b3|b4|b5|
# ----------------
# |c1|c2|c3|c4|c5|
# ----------------
# |d1|d2|d3|d4|d5|
# ----------------


zonename = ""
description = "description" # use only lowercase
examination = "examin" # use only lowercase
solved = False # use only lowercase
up = "up", "north" # use only lowercase
down = "down", "south" # use only lowercase
left = "left", "west" # use only lowercase
right = "right", "east" # use only lowercase

# key value DICTONARY a1 is KEY 
solved_places = {"a1": False, "a2": False, "a3": False, "a4": False,
                 "b1": False, "b2": False, "b3": False, "b4": False,
                 "c1": False, "c2": False, "c3": False, "c4": False,
                 "d1": False, "d2": False, "d3": False, "d4": False,
                 }

zonemap = {
    "a1": {
        zonename: "Town Market",
        description = "The town has a big market for it'S size."
        examination = "The market is busy today."
        solved = False
        up = ""
        down = "b1"
        left = ""
        right = "a2"
    },
    "a2": {
        zonename: "Town Entrance",
        description = "The gateway to the city."
        examination = "Many people come and go."
        solved = False
        up = ""
        down = "b2"
        left = "a1"
        right = "a3"
    },
    "a3": {
        zonename: "Town Square",
        description = "A big square in front of the administration building."
        examination = "There is an axecution sheduled for today. People are gathering."
        solved = False
        up = ""
        down = "b3"
        left = "a2"
        right = "a4"
    },
    "a4": {
        zonename: "Town Hall",
        description = "The administrative building of the whole region."
        examination = "A lot of people are visiting and doing business."
        solved = False
        up = ""
        down = "b4"
        left = "a3"
        right = ""
    },
    "b1": {
        zonename: "",
        description = "description"
        examination = "examin"
        solved = False
        up = "a1"
        down = "c1"
        left = ""
        right = "b2"
    },
    "b2": {
        zonename: "Home",
        description = "This is your home!"
        examination = "Your home looks the same - nothing has changed."
        solved = False
        up = "a2"
        down = "c2"
        left = "b1"
        right = "b3"
    },
    "b3": {
        zonename: "",
        description = "description"
        examination = "examin"
        solved = False
        up = "a3"
        down = "c3"
        left = "b2"
        right = "b4"
    },
    "b4": {
        zonename: "",
        description = "description"
        examination = "examin"
        solved = False
        up = "a4"
        down = "c4"
        left = "b3"
        right = ""
    },
    "c1": {
        zonename: "",
        description = "description"
        examination = "examin"
        solved = False
        up = "b1"
        down = "d1"
        left = ""
        right = "c2"
    },
    "c2": {
        zonename: "",
        description = "description"
        examination = "examin"
        solved = False
        up = "b2"
        down = "d2"
        left = "c1"
        right = "c3"
    },
    "c3": {
        zonename: "",
        description = "description"
        examination = "examin"
        solved = False
        up = "b3"
        down = "d3"
        left = "c2"
        right = "c4"
    },
    "c4": {
        zonename: "",
        description = "description"
        examination = "examin"
        solved = False
        up = "b4"
        down = "d4"
        left = "c3"
        right = ""
    },
    "d1": {
        zonename: "",
        description = "description"
        examination = "examin"
        solved = False
        up = "c1"
        down = ""
        left = ""
        right = "d2"
    },
    "d2": {
        zonename: "",
        description = "description"
        examination = "examin"
        solved = False
        up = "c2"
        down = ""
        left = "d1"
        right = "d3"
    },
    "d3": {
        zonename: "",
        description = "description"
        examination = "examin"
        solved = False
        up = "c3"
        down = ""
        left = "d2"
        right = "d4"
    },
    "d4": {
        zonename: "",
        description = "description"
        examination = "examin"
        solved = False
        up = "c4"
        down = ""
        left = "d3"
        right = ""
    },
}