import random
import time

difficulty = 0
balance = 0
go = 0

while True:
    ds = input('''Choose a difficulty:
1. Baby
2. Normal
3. Realistic
''')
    if ds == '1':
        difficulty = 0.5
        balance = 3500
    elif ds == '2':
        difficulty = 1
        balance = 2500
    elif ds == '3':
        difficulty = 3
        balance = 1000
    else:
        print('Not a valid response')
        continue
    break

ga = int(input('How much do you want to gamble with? '))

while ga <= balance:
    go += 1
    balance -= ga
    print(balance)
    time.sleep(0.05)

