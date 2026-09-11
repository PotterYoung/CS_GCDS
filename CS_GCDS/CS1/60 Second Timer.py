import time
import os
import sys
import random

def type_text(text, speed=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)

while True:
    try:
        timer = int(input('''Imput a number to count down from
'''))
        break
    except ValueError:
        print('Please enter an integer')

if os.name == 'nt':
    os.system('cls')

while timer > 0:
    print(timer)
    timer -= 1
    time.sleep(1)

if timer < 0:
    type_text("A negative integer was imputed...", 0.1)
    type_text(" SELF DESTRUCTING!!! ", 0.2)
    type_text("Just kidding!", 0.1)
else:
    print("TIMER DONE!!!")