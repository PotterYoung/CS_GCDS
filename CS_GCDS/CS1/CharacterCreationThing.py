# Setup
import sys
import random
import time
import os

def type_text(text, speed=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)

def type_text_fast(text, speed=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)

def type_text_slow(text, speed=0.25):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)

# Stats
c_speed = 0
c_strength = 0
c_defense = 0
c_hope = 0
c_intelligence = 0
c_class = "none"

# Character Creation
type_text('''Welcome wandering soul, let me help give you a host. Please answer with numbers.
''')
time.sleep(0.5)
type_text('''...
''')
time.sleep(0.5)

# Question 1
while True:
    type_text('''What body size do you choose?
''')
    type_text_fast('''1. Tall
2. Small''')
    cc_1 = input('''
''')

    if cc_1 == "1":
        c_speed += 5
        c_strength += 4
        c_defense += 7
    elif cc_1 == "2":
        c_speed += 10
        c_strength += 3
        c_defense += 3
    else:
        type_text_fast('''Do not be difficult, this is not a valid answer.
''')
        continue
    break

# Question 2
while True:
    time.sleep(0.5)
    type_text('''...
''')
    time.sleep(0.5)

    type_text('''What trait will you give it?
''')
    type_text_fast('''1. Empathy
2. Strength
3. Intelligence
4. Agility''')
    cc_2 = input('''
''')
    if cc_2 == "1":
        c_hope += 1
    elif cc_2 == "2":
        c_strength += 3
    elif cc_2 == "3":
        c_intelligence += 5
    elif cc_2 == "4":
        c_speed += 3
    else:
        type_text_fast('''Do not be difficult, this is not a valid answer. 
''')
        continue
    break

# Question 3
while True:
    time.sleep(0.5)
    type_text('''...
''')
    time.sleep(0.5)

    type_text('''What virtue is its pursuit?
''')
    type_text_fast('''1. Humility
2. Chastity
3. Temperance
4. Charity
5. Diligence
6. Patience
7. Kindess''')
    cc_3 = input('''
''')
    if (cc_3 == "1" or cc_3 == "3" or cc_3 == "6"):
        c_hope += 1
        c_intelligence += 3
        break
    elif (cc_3 == "2" or cc_3 == "4" or cc_3 == "7"):
        c_hope += 2
        c_strength += 3
        break
    elif cc_3 == "5":
        c_strength =+ 4
        c_hope += 1
        break
    else: 
        type_text_fast('''Do not be difficult, this is not a valid answer. 
''')
        continue

# Question 4
while True:
    time.sleep(0.5)
    type_text('''...
''')
    time.sleep(0.5)

    type_text('''What sin does it embody?
''')
    type_text_fast('''1. Pride
2. Greed
3. Wrath
4. Envy
5. Lust
6. Gluttony
7. Sloth''')
    cc_4 = input('''
''')
    if (cc_4 == "1" or cc_4 == "3"):
        c_strength += 4
        c_hope -= 1
        c_speed += 2
        break
    elif (cc_4 == "4" or cc_4 == "5" or cc_4 == "2" or cc_4 == "6"):
        c_hope -= 1
        c_speed += 4
        c_strength += 2
        break
    elif cc_4 == "7":
        c_speed -= 4
        c_defense += 6
        break
    else: 
        type_text_fast('''Do not be difficult, this is not a valid answer. 
''')
        continue

# Question 5
while True:
    time.sleep(0.5)
    type_text('''...
''')
    time.sleep(0.5)

    type_text('''What is its class?
''')
    type_text_fast('''1. Blademaster
2. Mechanic
3. Mage
4. Sharpshooter
5. Ringmaster''')
    cc_5 = input('''
''')
    if cc_5 == "1":
        c_class = "Blademaster"
    elif cc_5 == "2":
        c_class = "Mechanic"
    elif cc_5 == "3":
        c_class = "Mage"
    elif cc_5 == "4":
        c_class = "Sharpshooter"
    elif cc_5 == "5":
        c_class = "Ringmaster"
    else:
        type_text_fast('''Do not be difficult, this is not a valid answer. 
''')
        continue
    break

# Result
time.sleep(0.5)
type_text('''...
''')
time.sleep(0.5)
type_text('''What an interesting vessel you have created.
''')
time.sleep(0.5)
type_text('''... 
''')
time.sleep(0.5)
type_text_slow("It will now be discarded...")
if os.name == 'nt':
    os.system('cls')
type_text("THEY have already chosen who you are.")
quit()