# The idea: medieval theming (instead of water with ships like a kingdom with buildings), player vs player, 
# when a place is hit there's like a fire, playsound for like the sounds and stuff
# before the rows on the print board function do like A and 1 like a google sheet
# make it blank between each turn with a press enter to continue to switch each player's turn
# maybe have optional challenges/other modes like a certain square that instantly loses you the game and other stuff

import os
import random
import time
import playsound

def main():
    winner = -1
    p1_def_board = [[' ', ' ' , ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' '], 
                    [' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ']]
    
    p1_atk_board = [[' ', ' ' , ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' '], 
                    [' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ']]
    
    p2_def_board = [[' ', ' ' , ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' '], 
                    [' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ']]
    
    p2_atk_board = [[' ', ' ' , ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' '], 
                    [' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ']]

    print('Enter a name for player 1')
    while True:
        p1_name = input('')
        if p1_name == '':
            print('Please enter a name')
        else:
            break
    print('Enter a name for player 2')
    while True:
        while True:
            p2_name = input('')
            if p2_name == '':
                print('Please enter a name')
            else:
                break
        if p2_name.lower() == p1_name.lower():
            print('Please enter a unique name')
        else:
            break



    place_dots(p2_def_board, 5)
    place_dots(p1_def_board, 5)
    for i in range(10):
        print(f'{10-i} turns remaining!\n')
        player_turn(p1_def_board, p1_atk_board, p2_def_board)
        if dots_remaining(p2_def_board) == 0:
            winner = 1
            break
        print(f'{10-i} turns remaining!\n')
        player_turn(p2_def_board, p2_atk_board, p1_def_board)
        if dots_remaining(p1_def_board) == 0:
            winner = 2
            break
    if os.name == 'nt':
        os.system('cls')
    if winner == 1:
        print(f'{p1_name} has won!')
        playsound.playsound('confetti.mp3')
    elif winner == 2:
        print(f'{p2_name} has won!')
        playsound.playsound('confetti.mp3')
    else:
        print('Tie')

def print_board(board):
    print('  A   B   C   D   E')
    for row in range(4):
        print(f'{row+1} {board[row][0]} | {board[row][1]} | {board[row][2]} | {board[row][3]} | {board[row][4]}')
        print('  -----------------')
    print(f'5 {board[4][0]} | {board[4][1]} | {board[4][2]} | {board[4][3]} | {board[4][4]}')

def clear_board():
    # make sure to do the board = clear_board(board)
    board = [[' ', ' ' , ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' '], 
            [' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ']]
    return board

def player_turn(pl_def_board, pl_atk_board, en_board):
    hit = False
    print('Your base:')
    print_board(pl_def_board)
    print('\n=====================\n')
    print('Fire here:')
    print_board(pl_atk_board)
    result = fire_shot(pl_atk_board, en_board)
    if result == True:
        print('Hit!')
        playsound.playsound('boom.mp3')
        hit = True
    elif result == -1:
        print('That place has already been hit')
        hit = False
        time.sleep(.5)
    else:
        print('Miss!')
        hit = False
        time.sleep(.5)
    if os.name == 'nt':
        os.system('cls')
    input('Press enter to continue to the next players turn')
    if os.name == 'nt':
        os.system('cls')
    if hit == True:
        print('Youve been hit!')

def place_dots(board, dot_amount, dot_symbol = 'O'):
    for i in range(dot_amount):
        while True:
            col_cord = random.randint(0,4)
            row_cord = random.randint(0,4)
            if board[row_cord][col_cord] == ' ':
                board[row_cord][col_cord] = dot_symbol
                break

def get_shot():
    print('Where do you want to shoot? (Use the correct format of A1-E5)')
    while True:
        shot_pos = input('').upper()
        if shot_pos == 'A1':
            return 0,0
        elif shot_pos == 'A2':
            return 1,0
        elif shot_pos == 'A3':
            return 2,0
        elif shot_pos == 'A4':
            return 3,0
        elif shot_pos == 'A5':
            return 4,0
        elif shot_pos == 'B1':
            return 0,1
        elif shot_pos == 'B2':
            return 1,1
        elif shot_pos == 'B3':
            return 2,1
        elif shot_pos == 'B4':
            return 3,1
        elif shot_pos == 'B5':
            return 4,1
        elif shot_pos == 'C1':
            return 0,2
        elif shot_pos == 'C2':
            return 1,2
        elif shot_pos == 'C3':
            return 2,2
        elif shot_pos == 'C4':
            return 3,2
        elif shot_pos == 'C5':
            return 4,2
        elif shot_pos == 'D1':
            return 0,3
        elif shot_pos == 'D2':
            return 1,3
        elif shot_pos == 'D3':
            return 2,3
        elif shot_pos == 'D4':
            return 3,3
        elif shot_pos == 'D5':
            return 4,3
        elif shot_pos == 'E1':
            return 0,4
        elif shot_pos == 'E2':
            return 1,4
        elif shot_pos == 'E3':
            return 2,4
        elif shot_pos == 'E4':
            return 3,4
        elif shot_pos == 'E5':
            return 4,4
        else:
            print('Invalid input')

def dots_remaining(board):
    rem_dots = 0
    for row in range(5):
        for column in range(5):
            if board[row][column] == 'O':
                rem_dots += 1
    return rem_dots

def ai_shot(ai_board, en_board):
    while True:
        cords = random.randint(0,4), random.randint(0,4)
        if ai_board[cords[1]][cords[0]] == ' ':
            break
    if en_board[cords[1]][cords[0]] == ' ':
        ai_board[cords[1]][cords[0]] = '-'
        return False
    else:
        ai_board[cords[1]][cords[0]] = '✴︎'
        en_board[cords[1]][cords[0]] = '✴︎'
        return True

def fire_shot(pl_board, en_board):
    cords = get_shot()
    cord_row = cords[0]
    cord_col = cords[1]
    playsound.playsound('cannon.mp3')
    if en_board[cord_row][cord_col] == ' ':
        pl_board[cord_row][cord_col] = '-'
        return False
    elif pl_board[cord_row][cord_col] == '✴︎':
        return -1
    else:
        pl_board[cord_row][cord_col] = '✴︎'
        en_board[cord_row][cord_col] = '✴︎'
        return True

def count_dots(board):
    dots_left = 0
    for row in range(5):
        for column in range(5):
            if board[row][column] == 'X':
                dots_left += 1
    return dots_left

main()