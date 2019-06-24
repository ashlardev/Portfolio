# RPG Game
# Author: ScrapPY

# Imports
import cmd
import textwrap
import sys
import os
import time
import random

# Global Variables
screen_width = 100
Caitlyn = Player()
Chris = Player()

### Player Setup ###
class Player:
    def __init__(self):
        self.name = ''
        self.age = ''
        self.race = ''
        self.pclass = ''
        self.hp = 0
        self.mp = 0
        self.status_effects = []
        self.location = 'a dark and lonely room...'



### Title Screen ###
def title_screen_selections():
    option = input('> ')
    while option.lower() not in ['play', 'help', 'quit']:
        print('Please enter a valid command.')
    if option.lower() == ('play'):
        start_game() # placeholder until written
    elif option.lower() == ('help'):
        help_menu() # placeholder until written
    elif option.lower() == ('quit'):
        sys.exit()

def title_screen():
    os.system('cls')
    print('#######################################')
    print('# Welcome to my python based RPG Game #')
    print('#######################################')
    print('#            - Play -                 #')
    print('#            - Help -                 #')
    print('#            - Quit -                 #')
    print('#######################################')
    title_screen_selections()

def help_menu():
    os.system('cls')
    print('#######################################')
    print('# Welcome to my python based RPG Game #')
    print('#######################################')
    print('# - Use up, down, left, right to move #')
    print('# - Type your commands to do them     #')
    print('# - Use "look" to inspect something   #')
    print('#######################################')
    print('#            - Play -                 #')
    print('#            - Quit -                 #')
    print('#######################################')
    title_screen_selections()

title_screen()



### Game Interactivity ###
def print_location():
    print('\n' + ('#' * (4 + len(Caitlyn.location))))
    print('\n' + Caitlyn.location.upper() + ' #')
    print('\n' + zonemap([Caitlyn.position][DESCRIPTION] + ' #')
    print('\n' + ('#' * (4 + len(Caitlyn.location))))
    print('\n')

def prompt():
    print('\n' + '################################################')
        print('What would you like to do?')
        action = input('> ')
        acceptable_action = ['move', 'go', 'travel', 'walk', 'quit', 'examine', 'inspect', 'interact', 'look']
        while action.lower() not in acceptable_actions:
            print('Unknown action, try again.\n')
            action = input('> ')
        if action.lower() == 'quit':
            sys.exit()
        elif action.lower() in ['move','go','travel','walk']:
            player_move(action.lower())
        elif action.lower() in ['examine', 'inspect', 'interact', 'look']:
            player_examine(action.lower())

def player_move(myAction):
    ask = 'Where would you like to move to?\n'
    dest = input(ask)
    if dest == 



### Game Functionality ###
def start_game():
    return

NAME = ''
DESCRIPTION = 'description'
EXAMINATION = 'examine'
SOLVED = False
UP = 'up', 'north'
DOWN = 'down', 'south'
LEFT = 'left', 'west'
RIGHT = 'right', 'east'

solved_places = {
    'a1': False, 'a2': False, 'a3': False, 'a4': False,
    'b1': False, 'b2': False, 'b3': False, 'b4': False,
    }

zonemap = {
    'a1': {
        ZONENAME: 'Outside',
        DESCRIPTION = 'It is raining, wouldn\'t you like to stay in the dry?'
        EXAMINATION = 'Just a shitty as the inside, pal!'
        SOLVED = False
        UP = ''
        DOWN = 'b1'
        LEFT = ''
        RIGHT = 'a2'
    },
    'a2': {
        ZONENAME: 'Living Room',
        DESCRIPTION = 'A milk crate sits in the middle of the empty, yet cramped space framing the tv perfectly.'
        EXAMINATION = 'where is the damn remote?'
        SOLVED = False
        UP = ''
        DOWN = 'b2'
        LEFT = 'a1'
        RIGHT = 'a3'
    },    
    'a3': {
        ZONENAME: 'Kitchen',
        DESCRIPTION = 'Small, sanitary, definitely not a woman\'s touch'
        EXAMINATION = 'Clean your dishes, the sink is full!'
        SOLVED = False
        UP = ''
        DOWN = 'b3'
        LEFT = 'a2'
        RIGHT = ''
    },       
    'b1': {
        ZONENAME: 'Bedroom',
        DESCRIPTION = 'An airmattress lays half inflated in the center of the floor.'
        EXAMINATION = 'There is a sock stood up in the corner! Yuck!!!'
        SOLVED = False
        UP = 'a1'
        DOWN = ''
        LEFT = ''
        RIGHT = 'b2'
    },    
    'b2': {
        ZONENAME: 'Home',
        DESCRIPTION = 'This is your home, the dark lonely room...'
        EXAMINATION = 'Use your imagination!'
        SOLVED = False
        UP = 'a2'
        DOWN = ''
        LEFT = 'b1'
        RIGHT = 'b3'
    },    
    'b3': {
        ZONENAME: 'Bathroom',
        DESCRIPTION = 'Such a disgusting and pathetic room...'
        EXAMINATION = 'Flush the toilet, you animal!'
        SOLVED = False
        UP = 'a3'
        DOWN = ''
        LEFT = 'b2'
        RIGHT = ''
    }
    }

