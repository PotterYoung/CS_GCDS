""""
┌───────────────────────────────────────────────────────────────────────────┐
│                            Joke Generator                                 │
├───────────────────────────────────────────────────────────────────────────┤
│ Name: Potter Young                                                        │
| Course: CS1                                                               |
│ Log: Finished project (1.0)                                               |
| Bugs: N/K                                                                 │
│ Description:  A program that generates a random joke from a selected      |
| from a list. Tt has two modes; a mode that selects normally from a list,  |
| and a mode that randomizes setups and punchlines                          |
└───────────────────────────────────────────────────────────────────────────┘
"""


import random
import sys
import time

setups = ['Why did the chicken cross the road?', 'A guy walks into a bar and says...', 'Road work ahead?', 'Exercise? I thought you said...', 'What do pirates say when they turn eighty?', 'What did one hat say to the other?', 'Why are mushrooms always invited out to parties?', 'Why should you never trust an atom?', 'Why did the frog ride a bike to school?', 'What do you call an apology in dots and lines?']
punchlines = ['To get to the other side!!!', 'Wait hold on where am I???', 'Yeah, I sure hope it does!', "EXTRA FRIES!!!", 'Aye matey!', 'You stay, I will go on a head', 'They are very fungis!', 'They make up everything!!', 'Their car was toad', 'Remorse code!']
s_funny_values = [1, 3, 6, 8, 10, 5, 2, 7, 4, 9]
p_funny_values = [2, 4, 5, 3, 8, 7, 1, 6, 10, 9]

total_rating = 0

def type_text(text, speed=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)

while True:
    mix_question = input('''Do you want to enable mix mode? (Y/N)
''')
    if mix_question.lower() == 'y':
        break
    elif mix_question.lower() == 'n':
        break

while True:
    try:
        joke_number = int(input('''How many jokes do you want? (Max 10)
'''))
        if joke_number > 10:
            type_text('''Please try a lower amount
''')
        else:
            break
    except ValueError:
        type_text('Please enter an integer')

if mix_question.lower() == 'n':
    for i in range(joke_number):
        setup = random.choice(setups)
        index = setups.index(setup)
        type_text(f'''{setup} {punchlines[index]} Joke Rating: {s_funny_values[index] * 10}
''')
        total_rating += s_funny_values[index] * 10
elif mix_question.lower() == 'y':
    for i in range(joke_number):
        setup = random.choice(setups)
        punchline = random.choice(punchlines)
        index = setups.index(setup)
        type_text(f'''{setup} {punchline} Joke Rating: {s_funny_values[index] * p_funny_values[index]}
''')
        total_rating += s_funny_values[index] * p_funny_values[index]
else:
    print("Something here broke, try restarting...")

type_text(f'Your final score is {total_rating}')