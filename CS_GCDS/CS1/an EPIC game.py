import random
import os
import time
import sys

difficulty = 0
ody_mode = False
debug = False

def type(text, speed=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)

def type_color(text, color_name, speed=0.05):
        
    colors = {
        'black': '\033[30m',    # Black text color
        'red': '\033[31m',      # Red text color
        'green': '\033[32m',    # Green text color
        'yellow': '\033[33m',   # Yellow text color
        'blue': '\033[34m',     # Blue text color
        'magenta': '\033[35m',  # Magenta (purple) text color
        'cyan': '\033[36m',     # Cyan text color
        'white': '\033[37m',    # White text color
        'reset': '\033[0m',     # Reset text color to default
    }
    
    color_code = colors.get(color_name.lower(), '\033[37m')
    for char in text:
        sys.stdout.write(f"{color_code}{char}\033[0m")
        sys.stdout.flush()
        time.sleep(speed)

if os.name == 'nt':
    os.system('cls')

while True: # Name STUFF
    type('''What is your name?
''')
    name = input()

    if name.lower() == "penelope":
        type_color('Lets cut the charade you are NO WIFE OF MINE.', 'red')
    elif name.lower() == "polities":
        type_color('I can tell youre getting nervous', 'cyan')
    elif name.lower() == "hermes":
        type_color('That names a little bit dangerous my friend!', 'yellow')
    elif name.lower() == "circe":
        type_color('No im not a player, im a puppeteer', 'magenta')
    elif name.lower() == "zeus":
        type_color('No.', 'yellow',0.5)
        exit()
    elif name.lower() == "telemachus":
        type('Hello Telemarketing! ')
        type('Teleportation? ', 0.075)
        type('Telecommunication?? ', 0.1)
        type('Telegraphing??? ', 0.125)
        type('Okay I give up...')
    elif name.lower() == "calypso":
        type_color('Here to entertain!', 'magenta')
    elif name.lower() == "tiresias":
        t_chance = random.randint(1,100)
        if t_chance < 100:
            type_color('You chose this name, but its no longer you', 'green')
        else:
            type_color('I knew youd say that', 'green')
    elif name.lower() == "athena":
        type_color('Well done, enlighten me, whats your name?', 'blue')
    elif name.lower() == "hephaestus":
        type_color('This name isnt given, its forged. Why should I give you my support?', 'black')
    elif name.lower() == "hera":
        type_color('So many names, so many are fine. Give me one good reason, why you chose MINE...', 'green')
    elif name.lower() == "aeolus":
        type_color('Hahaha! If you wanna get this name well I gotta say "no sir!"', 'cyan')
    elif name.lower() == "poseidon":
        type_color('I try to chill with the waves, but damn you crossed a line.', 'blue')
    elif name.lower() == "debug":
        debug = True
    else:
        break
    time.sleep(2)
    if os.name == 'nt':
        os.system('cls')
    continue

while True: # Difficulty Options
    type('''
How difficult do you want your journey? (Easy, Normal, or Hard)
''')
    difficulty_choice = input()

    if name.lower() == "odysseus":
        if difficulty_choice.lower() == "easy":
            type('You think his journey was easy? You dont get that luxury.')
        elif difficulty_choice.lower() == "normal":
            type('His journey was anything but normal, so neither will yours.')
        elif difficulty_choice.lower() == "hard":
            type('His journey was hard, but these difficulties dont measure. How about a REAL challenge?')
        elif difficulty_choice.lower() == "happy":
            type('Happiness isnt possible if your name is Odysseus, idiot')
        else:
            type('Your response never mattered anyways.')
        ody_mode = True
        difficulty = 3
        break
    elif difficulty_choice.lower() == "easy":
        difficulty = 0.75
    elif difficulty_choice.lower() == "normal":
        difficulty = 1
    elif difficulty_choice.lower() == "hard":
        difficulty = 1.5
    else:
        type('Insufficient response, try again.')
        continue
    break

time.sleep(1)
if os.name == 'nt':
    os.system('cls')

type('The carnage lays bare, Troy is no more. Countless warriors slain and buildings destroyed, but its finally over.'
'But suddenly, a voice rings in your head...')
type_color('''
Troy is sacked, yet a threat still remains.
''', 'yellow', 0.1)
type('The voice guides you to an unthreatening sight.')
type_color('''
Your final enemy is here, one that could avenge all of Troy if you let him live.
''', 'yellow', 0.1)
type('Infront of you is')
type('... A baby', 0.15)