import random
import time
import os
import sys

def color_text(text, color_name):
    """
    Print the given text in a specified color.
    
    Args:
        text (str): The text to be printed.
        color_name (str): The color of the text to be printed.
    """
        
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
    return f"{color_code}{text}\033[0m"

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

def type(text, speed=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)

apollo_convinced = False
hephaestus_convinced = False
aphrodite_callforboyfriend = False
aphrodite_convinced = False
ares_convinced = False
hera_convinced = False

round = 1

while round == 1: # APOLLO!!!
    if os.name == 'nt':
        os.system('cls')
    type_color('''Apollo!
''', 'white')
    type_color('You all know im a fan of catchy songs, but with so many sirens gone I think odys in the wrong', 'yellow')
    type_color('''
1. Argue
2. Appeal
3. Explain
''', 'white', 0.025)
    while apollo_convinced == False:
        apollo_response = input('')

        if (apollo_response == "1" or apollo_response.lower() == "argue"):
            type_color('''Those sirens forced him to kill them!
''', 'blue')
            type_color('He chose to cut their tails and left them to drown.', 'yellow')

        elif (apollo_response == "2" or apollo_response.lower() == "appeal"):
            type_color('''He's a great muscisian, he would easily be able to play the songs the sirens no longer can!
''', 'blue')
            type_color('I dont think he could replace them all.', 'yellow')

        elif (apollo_response == "3" or apollo_response.lower() == "explain"):
            type_color('''They were trying to do him worse, all he did was reimburse them. Now they'll tread with caution first,  to live another day and sing another verse
''', 'blue')
            time.sleep(0.5)
            type_color('If thats true, release him!', 'yellow')
            time.sleep(2)
            apollo_convinced = True

        else:
            print('Please enter a proper response!')
            continue

        round = 2

while round == 2: # Hephaestus.
    if os.name == 'nt':
        os.system('cls')
    type_color('''Hephaestus.
''', 'white')
    type_color('Trust isnt given its forged, why should I give him my support? He sacrificed his own cohort.', 'black')
    type_color('''
1. Argue
2. Appeal
3. Explain
''', 'white', 0.025)
    while hephaestus_convinced == False:
        hephaestus_response = input('')

        if (hephaestus_response == "1" or hephaestus_response.lower() == "argue"):
            type_color('''Did you forget they failed to listen? He was betrayed and then imprisoned. But if you make the right decision, he can still build a future 
with those who miss him
''', 'blue')
            time.sleep(0.5)
            type_color('Fine, release him.', 'black')
            time.sleep(2)
            hephaestus_convinced = True

        elif (hephaestus_response == "2" or hephaestus_response.lower() == "appeal"):
            type_color('''His trust was broken by those around him, he needs this help
''', 'blue')
            type_color('And he got back at them by forsakenening their lives? Im not convinced.', 'black')

        elif (hephaestus_response == "3" or hephaestus_response.lower() == "explain"):
            type_color('''He forged the trust with them over years, its their fault they didnt trust him enough.
''', 'blue')
            type_color('He broke that trust when he sacrificed their lives for his.', 'black')

        else:
            print('Please enter a proper response!')
            continue

        round = 3

while round == 3: #Aphrodite!
    if os.name == 'nt':
        os.system('cls')
    print('Aphrodite!')
    type_color('Your little high and mighty "Odysseus" claims to love his mother, but let her die of a broken heart.', 'magenta')
    type('''
1. Argue
2. Appeal
3. Explain
''', 0.025)
    while aphrodite_callforboyfriend == False:
        aphrodite_response = input('')

        if (aphrodite_response == "1" or aphrodite_response.lower() == "argue"):
            type_color('''He was busy fighting!
''', 'blue')
            type_color('More like busy spiting the cyclops, let him feel the pain his mother felt and rot.', 'magenta')
            aphrodite_callforboyfriend = True

        elif (aphrodite_response == "2" or aphrodite_convinced.lower() == "appeal"):
            type('''-
''')
            type('-')

        elif (aphrodite_response == "3" or aphrodite_convinced.lower() == "explain"):
            type('''-
''')
            type('-')

        else:
            print('Please enter a proper response!')
            continue

        round = 4

while round == 4:
    print('lalalalalalala')
    exit()