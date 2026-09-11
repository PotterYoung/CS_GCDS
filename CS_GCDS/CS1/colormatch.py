import random

def color_text(text, color_name):
    colors = {                  
        'black': '\033[30m',    
        'red': '\033[31m',      
        'green': '\033[32m',   
        'yellow': '\033[33m',  
        'blue': '\033[34m',     
        'magenta': '\033[35m', 
        'cyan': '\033[36m',    
        'white': '\033[37m',   
        'reset': '\033[0m',   
    }
    
    color_code = colors.get(color_name.lower(), '\033[37m')
    return f"{color_code}{text}\033[0m"

name = input("What is your name? ")
print(f"Hello {name}, the goal of this game is to type the color of the text written, not the text itself!")

colors = ["black", "red", "green", "yellow", "blue", "magenta", "cyan", "white"]
rounds = 0
correct = 0

while True:
    color = random.choice(colors)
    text_color = random.choice(colors)
    print(color_text(text_color, color))
    guess = input('''Quick! Enter the color of the text! ''').lower()

    if guess == color:
        print("You got it!")
        correct += 1
    else:
        print("Wrong!!")
    rounds += 1

    print(f'''{name} you got {correct} correct out of {rounds} rounds!
''')
    
    while True:
        play_again = input("Would you like to play again? (Y/N): ").lower()
        if play_again == "n":
            exit()
        elif play_again == "y":
            break
        else:
            print("Please enter a valid response")