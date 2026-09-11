import random
import time

while True: # Forever Loop
    question = input('''Ask the magic 8-ball a question (Make sure to include a question mark)
''') # Ask the initial question and store the input as a variable

    responses = ["I'd say so", "HELL NO", "Possibly", "I didn't get that", "HMMMMMMMM I don't know", "Hell if I know", "YES YES YES", "Probably", "Probably not", "Let me ask my boss", "False, no", "Nope", "No, why would you even ask such a STUPID question. Sorry that was rude :(", "Sorry I wasn't paying attention", "Yea", "NOOOOO", "Yesssssssssss"]
    # ^ Make a list of possible responses to put
    print("Thinking...") # Simulate a "Thinking" process
    time.sleep(1) # Same as above
    print(random.choice(responses)) # Print out a random response from the list of responses
    print("----------------------") # Make a split to seperate each question