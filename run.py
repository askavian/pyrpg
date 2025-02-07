# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

# Python Text RPG
# by Malte M. Boettcher

import cmd # imports command functions NOT USED ATM
import textwrap # displays text in wraps NOT USED ATM
import sys # imports system functions
import os # imports operating systems functions
import time # imports time related functions (counter, calender, clock, etc...)
import random # randomizes NOT USED ATM

screen_width = 100 # sets output window to full screen 100% width

#### Player Setup ####
class player:
    def __init__(self):
        self.name = ""
        self.job = ""
        self.hp = 0
        self.mp = 0
        self.status_effects =[] # empty array
        self.location = "b2" # sets location maybe use for case files
        self.game_over = False
myPlayer = player()

#### Title Screen ####
def title_screen_selections():
    option = input("> ")
    if option.lower() == ("play"):
        setup_game() # placeholder until written
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("quit"):
        sys.exit() # system function to exit program
    while option.lower() not in ["play", "help", "quit"]: # shows options while player is undecided
        print("Please enter a valid command.")
        option = input("> ")
        if option.lower() == ("play"):
            setup_game() # placeholder until written
        elif option.lower() == ("help"):
            help_menu()
        elif option.lower() == ("quit"):
            sys.exit() # system function to exit program

def title_screen():
    os.system("cls") # cls for windows "clear" for mac
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
        zonename: "Town Market", # SEMICOLON NEEDED? INDENTATION OK?
        description: "The town has a big market for it'S size.",
        examination: "The market is busy today.",
        solved: False,
        up: "",
        down: "b1",
        left: "",
        right: "a2",
    },
    "a2": {
        zonename: "Town Entrance",
        description: "The gateway to the city.",
        examination: "Many people come and go.",
        solved: False,
        up: "",
        down: "b2",
        left: "a1",
        right: "a3",
    },
    "a3": {
        zonename: "Town Square",
        description: "A big square in front of the administration building.",
        examination: "There is an axecution sheduled for today. People are gathering.",
        solved: False,
        up: "",
        down: "b3",
        left: "a2",
        right: "a4",
    },
    "a4": {
        zonename: "Town Hall",
        description: "The administrative building of the whole region.",
        examination: "A lot of people are visiting and doing business.",
        solved: False,
        up: "",
        down: "b4",
        left: "a3",
        right: "",
    },
    "b1": {
        zonename: "B1",
        description: "B1 description",
        examination: "B1 examin",
        solved: False,
        up: "a1",
        down: "c1",
        left: "",
        right: "b2",
    },
    "b2": {
        zonename: "Home",
        description: "This is your home!",
        examination: "Your home looks the same - nothing has changed.",
        solved: False,
        up: "a2",
        down: "c2",
        left: "b1",
        right: "b3",
    },
    "b3": {
        zonename: "B3",
        description: "B3 description",
        examination: "B3 examin",
        solved: False,
        up: "a3",
        down: "c3",
        left: "b2",
        right: "b4",
    },
    "b4": {
        zonename: "B4",
        description: "B4 description",
        examination: "B4 examin",
        solved: False,
        up: "a4",
        down: "c4",
        left: "b3",
        right: "",
    },
    "c1": {
        zonename: "C1",
        description: "C1 description",
        examination: "C1 examin",
        solved: False,
        up: "b1",
        down: "d1",
        left: "",
        right: "c2",
    },
    "c2": {
        zonename: "C2",
        description: "C2 description",
        examination: "C2 examin",
        solved: False,
        up: "b2",
        down: "d2",
        left: "c1",
        right: "c3",
    },
    "c3": {
        zonename: "C3",
        description: "C3 description",
        examination: "C3 examin",
        solved: False,
        up: "b3",
        down: "d3",
        left: "c2",
        right: "c4",
    },
    "c4": {
        zonename: "C4",
        description: "C4 description",
        examination: "C4 examin",
        solved: False,
        up: "b4",
        down: "d4",
        left: "c3",
        right: "",
    },
    "d1": {
        zonename: "D1",
        description: "D1 description",
        examination: "D1 examin",
        solved: False,
        up: "c1",
        down: "",
        left: "",
        right: "d2",
    },
    "d2": {
        zonename: "D2",
        description: "D2 description",
        examination: "D2 examin",
        solved: False,
        up: "c2",
        down: "",
        left: "d1",
        right: "d3",
    },
    "d3": {
        zonename: "D3",
        description: "D3 description",
        examination: "D3 examin",
        solved: False,
        up: "c3",
        down: "",
        left: "d2",
        right: "d4",
    },
    "d4": {
        zonename: "D4",
        description: "D4 description",
        examination: "D4 examin",
        solved: False,
        up: "c4",
        down: "",
        left: "d3",
        right: "",
    },
}


#### GAME INTERACTIVITY ####
def print_location():
    print("\n" + ("#" * (4 + len(myPlayer.location)))) # "\n" prints everything on a new line / make # x 4 len(myPlayer.location) gets the LENGTH OF THE STRING of location
    print("# " + myPlayer.location.upper() + " #")
    print("# " + zonemap[myPlayer.location] [description] + " #")
    print("\n" + ("#" * (4 + len(myPlayer.location))))

def prompt():  ### This is where the player "does" everything
    print("\n" + "===================")
    print("What would you like to do?")
    action = input("> ")
    acceptable_actions = ["move", "go", "travel", "walk", "quit", "examine", "inspect", "interact", "look"]
    while action.lower() not in acceptable_actions:
        print("Unkonw action, try again.\n")
        action = input("> ")
    if action.lower() == "quit":
        sys.exit()
    elif action.lower() in ["move", "go", "travel", "walk"]:
        player_move(action.lower())
    elif action.lower() in ["examine", "inspect", "interact", "look"]:
        player_examine(action.lower())

def player_move(myAction):
    ask = "Where would you like top move to?\n" # Input Question gets printet
    dest = input(ask)
    if dest in ["up", "north"]:
        destination = zonemap[myPlayer.location] [up]
        movement_handler(destination) # function defined below
    elif dest in ["left", "west"]:
        destination = zonemap[myPlayer.location] [left]
        movement_handler(destination) # function defined below
    elif dest in ["east", "right"]:
        destination = zonemap[myPlayer.location] [right]
        movement_handler(destination) # function defined below
    elif dest in ["down", "south"]:
        destination = zonemap[myPlayer.location] [down]
        movement_handler(destination) # function defined below    


def movement_handler(destination): # updates the movement
    print("\n" + "You have moved to the " + destination + ".") # prints to the player a success message for movement
    myPlayer.location = destination # sets the new location equal to the destination
    print_location()

def player_examine(action):
    if zonemap[myPlayer.location] [solved]:
        print("You have already exhausted this zone.")
    else: # UP FOR EVERYTHING 
        print("PLACEHOLDER You can trigger a puzzle here!")


#### GAME FUNCTIONALITY ####
def main_game_loop():
    while myPlayer.game_over is False: # is can also be
        prompt()
        # HERE YOU CAN PUT IN IF PUZZLES ARE SOLVED; BOSS DEFESTED ETC...

#### SET UP GAME ####

def setup_game():
    os.system("cls") # cls for windows "clear" for mac

    ### NAME COLLECTING ###
    question1 = "Hello, what's your name?\n" # not print because everything will come naturally
    for character in question1:
        sys.stdout.write(character) # just works don't ask questions
        sys.stdout.flush() # just works don't ask questions
        time.sleep(0.05) # gives delay to input of 5 miliseconds
    player_name = input("> ") # could directly write to myPlayer.name, but keep it seperated to eventually add functionality later
    myPlayer.name = player_name

    ### JOB COLLECTING ###
    question2 = "Hello, what role do you want to play?\n" # not print because everything will come naturally
    question2added = "(You can play as a warrior, priest, or mage)\n"
    for character in question2:
        sys.stdout.write(character) # just works don't ask questions
        sys.stdout.flush() # just works don't ask questions
        time.sleep(0.05) # gives delay to input of 5 miliseconds
    for character in question2added:
        sys.stdout.write(character) # just works don't ask questions
        sys.stdout.flush() # just works don't ask questions
        time.sleep(0.01) # gives delay to input of 1 miliseconds
    player_job = input("> ") # could directly write to myPlayer.job, but keep it seperated to eventually add functionality later
    valid_jobs = ["warrior", "mage", "priest"]
    if player_job.lower() in valid_jobs:
        myPlayer.job = player_job
        print("You are now a " + player_job + "!\n")
    while player_job.lower() not in valid_jobs:
        player_job = input("> ")
        if player_job.lower() in valid_jobs:
            myPlayer.job = player_job
            print("You are now a " + player_job + "!\n")


    #### PLAYER STATS ####
    if myPlayer.job is "warrior": # USE FOR TIME REMAINING
        myPlayer.hp = 120
        myPlayer.mp = 20
    elif myPlayer.job is "mage":
        myPlayer.hp = 40
        myPlayer.mp = 120
    elif myPlayer.job is "priest":
        myPlayer.hp = 70
        myPlayer.mp = 70

    ### INTRODUCTION
    question3 = "Welcome, " + player_name + " the " + player_job + ".\n" # not print because everything will come naturally
    for character in question3:
        sys.stdout.write(character) # just works don't ask questions
        sys.stdout.flush() # just works don't ask questions
        time.sleep(0.05) # gives delay to input of 5 miliseconds

    speech1 = "Welcome to this fantasy world!\n"
    speech2 = "I hope it greets you well!\n"
    speech3 = "Just make sure you don't get too lost...\n"
    speech4 = "Hehehehe...\n"
    for character in speech1:
        sys.stdout.write(character) 
        sys.stdout.flush() 
        time.sleep(0.03) # pretty fast
    for character in speech2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03) # pretty fast
    for character in speech3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.1) # slower
    for character in speech4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.2) # a lot slower
    
    os.system("cls") # cls for windows "clear" for mac
    print("########################")
    print("#   Let's Start now!   #")
    print("########################")
    main_game_loop()

title_screen() # actually initiates the game, starts the title screen defined above