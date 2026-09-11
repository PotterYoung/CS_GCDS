# SETUP

import random

def color_text(text, color_name): # Set a function to create colored text
    """
    Print the given text in a specified color.
    
    Args:
        text (str): The text to be printed.
        color_name (str): The color of the text to be printed.
    """
        
    colors = {                  # Dictionary mapping color names to their ANSI escape codes for terminal text coloring
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
    
    color_code = colors.get(color_name.lower(), '\033[37m') # Get the ANSI color code for the given color name, defaulting to white if the color is not found
    return f"{color_code}{text}\033[0m"                     # Print the text with the specified color, followed by the reset code to ensure no color leaks


def print_colored_text(text, color_name):                   # Fixing prior naming to not break everything
    print(color_text(text, color_name))                     # Set "print_colored_text" to do the same as "color_text" 

sleepiness_value = 0                                        # Set variable of "sleepniness_value" for 0 to setup for sleepy ending and attempted productivity ending

# QUESTION 1: 
while True:                                                                                         # Forever loop
    resp1 = input('''(NOTE: PLEASE ANSWER IN NUMBERS) A loud banging wakes you up, what do you do? 
1. Get up 
2. Go back to sleep
''')                                                                                                # Print the first question and take the answer as a variable
    
    if resp1 == "1" and sleepiness_value >= 4:                                                      # Check if you've slept 4 times and attempted to get up
        print("You can't get up, too tired...")                                                     # Printing context
        print_colored_text('Attempted Productivity Ending', 'green')                                # Ending given
        exit()                                                                                      # Stop program
    
    elif resp1 == "2" and sleepiness_value >= 4:                                                    # Check if you've slept in over 4 times
        print("You slept in 5 times...")                                                            # Printing contesxt
        print_colored_text('Sleepy Ending', 'blue')                                                 # Ending given
        exit()                                                                                      # Stop program

    elif resp1 == "1":                                                                              # Check if the response was "Get Up"
        print('''You get up and look around your room
''')                                                                                                # Printing Context
        break                                                                                       # Breaking forever loop

    elif resp1 == "2":                                                                              # Check if the response was "Go back to sleep"
        print('''You decided to sleep in accomplishing nothing, as you will just wake up again...
''')                                                                                                # Printing Context
        sleepiness_value = sleepiness_value + 1                                                     # Adding "sleepiness_value" for the sleep ending and attempted productivity ending

    else:                                                                                           # Check if not a valid answer
        print('''Not a valid response try again
              ''')                                                                                  # Restarts question

# QUESTION 2: 
while True:                                                                                 # Forever loop
    resp2 = input('''You see your uncompleted homework and a cat. What do you do?
1. Be productive and do your uncompleted homework
2. Pet the cat
''')                                                                                        # Prompt question 2

    if resp2 == "1":                                                                        # Check if the response was "Be productive and do your uncompleted homework"
        print("You did your work and got a good grade...")                                  # Printing context
        print_colored_text('Boring Ending', 'black')                                        # Ending given
        exit()                                                                              # Stop program

    elif resp2 == "2":                                                                      # Check if the response was "Pet the cat"
        print('''The cat turns out to actually be two seperate cats!
''')                                                                                        # Printing Context
        break                                                                               # Breaking forever loop

    else:                                                                                   # Check if not a valid answer
        print('''Not a valid response try again
              ''')                                                                          # Restarts question

# QUESTION 3:
while True:                                                                                 # Forever loop
    print_colored_text('''1. Cat 1
      |\     /|
      |'\___/'|
      |=^   ^=|
      \=\_Y_/=/
       )  `  (    ,
      /       \  ((
      |       |   ))
     /| |   | |\_//
     \| |._.| |/-`
      '"'   '"'
''', 'cyan')
    print_colored_text('''2. Cat 2
    .       .         
    \`-"'"-'/
     ) 0 o (
    =.  Y  ,=   
      /^^^\  .
     /     \  )           
    (  )-(  )/ 
     ""   ""
''', 'magenta')                                                                       # Printing both cats
    resp3 = input('''Which of the two cats do you pet?
''')                                                                                  # Prompting which cat to choose
    
    if resp3 == "1":                                                                  # Check if response was cat 1
        print('''You pet the first cat, but its stomach starts to growl!!
''')                                                                                  # Printing Context
        break                                                                         # Break forever loop

    elif resp3 == "2":                                                                # Check if response was cat 2
        print('''You pet the second cat, and it starts GLOWING!!! AAAAAA!!!!
''')                                                                                  # Printing Context
        break                                                                         # Break forever loop
    
    else:                                                                             # If not a valid response
        print('''Not a valid response try again
              ''')                                                                    # Restarts question

# ROUTE 1:      
if resp3 == "1":                                                                # Check if you chose cat 1

    # QUESTION 1-1:
    while True:                                                                 # Forever loop
        resp1_1 = input('''Do you feed the cat?
1. Yes
2. No
''')                                                                            # Prompt question
    
        if resp1_1 == "1":                                                      # Check if you chose yes
            print('''You search the cubbords for food, but THERE IS NONE!!!
''')                                                                            # Printing Context
            break                                                               # Break forever loop
        
        elif resp1_1 == "2":                                                    # Check if you chose no
            print("You MONSTER the cat LEFT YOU because you didn't feed it...") # Printing Context
            print_colored_text('MEANIE Ending', 'red')                          # Give ending
            exit()                                                              # Close program

        else:                                                                   # If not a valid response
            print('''Not a valid response try again
              ''')                                                              # Restarts question
            
    # QUESTION 1-2:
    while True:                                                                                                                                                     # Forever loop
        resp1_2 = input('''How do you get food???
1. Feed your cat your homework
2. Go to the store
''')                                                                                                                                                                # Prompt question

        if resp1_2 == "1":                                                                                                                                          # Check if you chose "Feed your cat your homework"
            print("You fed your cat homework, and now they're full...")                                                                                             # Printing context
            print_colored_text('Chunky Cat Ending', 'yellow')                                                                                                       # Give ending
            exit()                                                                                                                                                  # Close program

        elif resp1_2 == "2":                                                                                                                                        # Check if you chose "Go to the store"
            print('''You go to the store, but you don't have any money!!
''')                                                                                                                                                                # Printing Context
            break                                                                                                                                                   # Break forever loop

        else:                                                                                                                                                       # If not a valid response
            print('''Not a valid response try again
              ''')                                                                                                                                                  # Restarts question
    
    # QUESTION 1-3:
    while True:                                                                                                                                                     # Forever loop
        resp1_3 = input('''How do you earn enough money for cat food?
1. Pet your cat on live television
2. ROB A BANK
''')                                                                                                                                                                # Prompt question
        if resp1_3 == "1":                                                                                                                                          # Check if you chose "Pet your cat on live television"
            print("You started petting your cat on television, and instantly become a viral success! You now have fans, money, and you forgot to feed your cat...") # Print long and sad context
            print_colored_text('Fame at What Cost? Ending', 'black')                                                                                                # Give ending
            exit()                                                                                                                                                  # Close program
        
        elif resp1_3 == "2":
            print("You went to rob a bank without any supplies, and were caught immediately...")                                                                    # Printing context
            print_colored_text('Arrested Ending', 'red')                                                                                                            # Give ending
            exit()                                                                                                                                                  # Close program

        else:                                                                                                                                                       # If not a valid response
            print('''Not a valid response try again
              ''')                                                                                                                                                  # Restarts question
            
# ROUTE 2
elif resp3 == "2":                                                                                                                                                  # Check if you chose cat 2

    # QUESTION 2-1:
    while True:                                                                                                                                           # Forever loop
        resp2_1 = input('''WHAT DO YOU DO AAAAAAA!!!
1. Go to the Vet
2. Go to the aliens that are mysteriously in your backyard
''') # Prompt question
        if resp2_1 == "1":                                                                                                                                # Check if you chose "Go to the Vet"
            print("You decided to go the the vet, they said they can fix the cat's glowing. It only costs $276,357, which you evidently can't afford...") # Printing context
            print_colored_text('Sickly Ending', 'green')                                                                                                  # Give ending
            exit()                                                                                                                                        # Close program

        elif resp2_1 == "2":                                                                                                                              # Check if you chose "Go to aliens that are mysteriously in your backyard"
            print('''The aliens say they can fix your cat for the price of 10 glorp coins
''')                                                                                                                                                      # Print context
            break                                                                                                                                         # Break forever loop

        else:                                                                                                                                             # If not a valid response
            print('''Not a valid response try again
              ''')                                                                                                                                        # Restarts question
            
    # QUESTION 2-2:
    while True:                                                                                                                                              # Forever loop
        resp2_2 = input('''How do you get 10 glorp coins?
1. Search in the dumpsters
2. Go into a parallel dimension where glorp coins are the normal currency and steal 10 from the alternate version of yourself to pay it off
''')                                                                                                                                                         # Prompt question
        if resp2_2 == "1":                                                                                                                                   # Check if you chose "Search in the dumpsters"
            print("You search the local dumpster, and found 11 glorp coins! You were able to payoff the bill and buy a really cool space blaster aswell...") # Printing context
            print_colored_text('Otherworldly Assistance Ending', 'blue')                                                                                     # Give ending
            exit()                                                                                                                                           # Close program

        elif resp2_2 == "2":                                                                                                                                 # Check if you chose "Go into a parallel dimension where glorp coins are the normal currency and steal 10 from the alternate version of yourself to pay it off"
            print('''You decide to go into a parallel dimension, but you are lacking a method to travel into one.
''')                                                                                                                                                         # Print context
            break                                                                                                                                            # Break forever loop

        else:                                                                                                                                                # If not a valid response
            print('''Not a valid response try again
              ''')                                                                                                                                           # Restarts question
            
    # QUESTION 2-3:
    while True:                                                                                                                                               # Forever loop
        resp2_3 = input('''How do you get one?
1. Steal from a scientist
2. Do your homework to figure it out
''')                                                                                                                                                          # Prompt question
        if resp2_3 == "1":                                                                                                                                    # Check if you chose "Steal from a scientist"
            print("You snuck into the scientists and come across a machine to take you into a parallel dimension. You and your cat enter the machine and...") # Printing strange and mysterious context
            
            string = ''                                                                                                                                       # Setting string to be empty

            for char in 'Traveler Ending':                                                                                                                    # Setting this as the value
                string += color_text(char, random.choice(['cyan', 'magenta', 'blue', 'white', 'black']))                                                      # Adding every character to the string as a random color
            
            print(string)                                                                                                                                     # Printing said string, giving the ending
            exit()                                                                                                                                            # Close program
        
        elif resp2_3 == "2":                                                                                                                                  # Check if you chose "Do your homework to figure it out"
            print("You decide to try and do your homework to figure out a solution... Boring Ending 2")                                                       # Printing context
            print_colored_text('Boring Ending 2', 'black')                                                                                                    # Give ending
            exit()                                                                                                                                            # Close program

        else:                                                                                                                                                 # If not a valid response
            print('''Not a valid response try again
              ''')                                                                                                                                            # Restarts question