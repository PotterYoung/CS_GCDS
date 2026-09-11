import random
import time

while True:
    responses = ["Yes", "No", "Maybe", "Ask Again"]
    input('''Ask the magic 8-ball a question
''')
    print("Thinking...")
    time.sleep(1)
    print(random.choice(responses))
    print("----------------------")