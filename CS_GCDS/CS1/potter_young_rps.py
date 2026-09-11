import random
import time

p_score = 0 # Set player score to 0
b_score = 0 # Set bot score to 0

win_phrases = ["DEMOLISHED", "DESTROYED", "EXECUTED", "EVISCIRATED", "OBLITIRATED", "won against"] # Create a list of phrases to play when winning a round
rps_list = ["Rock", "Paper", "Scissors"] # Create a list of possible choices for the bot

while p_score < 3 and b_score < 3: # Run only if both scores are beneath 3
    p_choice = input('''---------------------------------
Rock, Paper, Scissors
''').lower()
    
    if (p_choice =="rock" or p_choice =="paper" or p_choice =="scissors"): # Run if the player puts in a valid input (rock paper or scissors)
        b_choice = random.choice(rps_list) # Set the bot's choice to a random from the list of choices
        print("...")
        time.sleep(1) # Wait 1 second
        print("SHOOT!")
        print(f'{b_choice}!')

        if b_choice.lower() == p_choice.lower(): # Check if both inputs are the same
            print("Tie!")
        elif b_choice == "Rock" and p_choice == "scissors": # Check if bot beat player with r-s
            print("🪨 ",random.choice(win_phrases),"✂️")
            b_score += 1
        elif b_choice == "Rock" and p_choice == "paper": # Check if player beat bot with p-r
            print("📄",random.choice(win_phrases),"🪨" )
            p_score += 1
        elif b_choice == "Paper" and p_choice == "rock": # Check if bot beat player with p-r
            print("📄",random.choice(win_phrases),"🪨")
            b_score += 1
        elif b_choice == "Paper" and p_choice == "scissors": # Check if player beat bot with s-p
            print("✂️ ",random.choice(win_phrases),"📄")
            p_score += 1
        elif b_choice == "Scissors" and p_choice == "paper": # Check if bot beat player with s-p
            print("✂️ ",random.choice(win_phrases),"📄")
            b_score += 1
        elif b_choice == "Scissors" and p_choice == "rock": # Check if player beat bot with r-s
            print("🪨 ",random.choice(win_phrases),"✂️")
            p_score += 1            
        else: # Failsafe
            print("Invalid, try again")
            continue

        print(p_score, "to", b_score)

    else: # If not a valid input ask again
        print("Not an answer")

if p_score > b_score: # Check if when either score is 3 if player score is higher
    print("You win!")
else: # Check if when either score is 3 if bot score is higher
    print("You lose.")