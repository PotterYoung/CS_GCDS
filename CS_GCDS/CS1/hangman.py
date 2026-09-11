import random

word_list = ["red", "orange", "yellow", "green", "blue", "purple"]
round_word = random.choice(word_list)
print(round_word)
guesses = 3

display = []

for letter in round_word:
    display.append('_')
print(' '.join(display))

while guesses > 0 and '_' in display:
    guess = input('''Guess a letter!
''')
    if guess in round_word:
        for i in range(len(round_word)):
            if guess == round_word[i]:
                display[i] = guess
    else:
        print("Incorrect guess!!", guesses -1, "remain")
        guesses -= 1
    print(' '.join(display))
    

