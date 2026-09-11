import time
import random
import sys
import os

if os.name == 'nt':
    os.system('cls')

happiness = 100
money = 100
respect = 100
hunger = 100
day = 0
lose = False


def type_text(text, speed=0.075):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)

while day == 0:
    tutorialdeny = input('''Do you want an introduction? (Y/N)
''')
    if tutorialdeny.capitalize() == "Y":
        os.system('cls')
        type_text('''Welcome your majesty, you have a few duties as the king of this kingdom. You must keep the people happy so the citizens do
not start a riot, you must make sure there is enough funding for the kingdom so everything works as inteded, you must make sure people 
respect you and follow the rules, and you must feed the citizens to make sure they do not starve.''')
        day += 1
    elif tutorialdeny.capitalize() == "N":
        day += 1
    else:
        type_text('''That's not a valid answer...
''')

while lose == False:
    os.system('cls')

    type_text(f'''Day {day}
''')
    type_text(f"Happiness = {happiness}, Money = {money}, Respect = {respect}, Hunger = {hunger}")
    time.sleep(1)
    event = random.randint(1,20)

    if event == 1:
        type_text('''
A man cloud in shadow is rumored to have killed a few citizens, the kingdom is now in panic.''')
    elif event == 2:
        type_text('''
A thief came into town and stole some of the bread reserves!''')
        hunger += 15
    elif event == 3:
        type_text('''
A merchant came in and gave the kingdom valuable resources!''')
    elif event == 4:
        type_text('''
A neighbouring kingdom decided you seem like an invaluable ally, do you accept their offer?''')
        input('''
''')
    else:
        type_text('''
Screw you, game OVER or something''')
        happiness = -100

    if happiness >= 100:
        happiness = 100
    if respect >= 100:
        respect = 100
    if hunger >= 100:
        hunger = 100

        if hunger * respect * money * happiness <= 0:
            lose = True

    input('''
''')
    
    day += 1

if lose == True:
    type_text(f"You lose! Days: {day - 1}")
    exit()