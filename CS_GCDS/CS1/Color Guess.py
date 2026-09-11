import random
color_list = ["turquoise", "rose", "violet", "gold", "cyan"]
tries = 0
color = random.choice(color_list)

while tries < 4:
    guess = input('''Guess the color!
''').lower()
    
    if guess == color:
        print(f"You got it in {tries + 1} tries!")
        print("You win!")
        exit()
    else:
        print(f"Wrong color! You have {3 - tries} tries remaining!")
        tries += 1

print("You lose")