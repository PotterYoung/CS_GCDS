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

    place_dots(p1_def_board, 5)
    print_board(p1_def_board)
    print(fire_shot(p1_def_board))
    print(fire_shot(p1_def_board))
    print(fire_shot(p1_def_board))
    print(fire_shot(p1_def_board))
    print(fire_shot(p1_def_board))

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

def place_dots(board, dot_amount):
    for i in range(dot_amount):
        while True:
            col_cord = random.randint(0,4)
            row_cord = random.randint(0,4)
            if board[row_cord][col_cord] == ' ':
                board[row_cord][col_cord] = 'X'
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

def fire_shot(en_board):
    cords = get_shot()
    cord_row = cords[0]
    cord_col = cords[1]
    if en_board[cord_row][cord_col] == ' ':
        return False
    else:
        en_board[cord_row][cord_col] = 'O'
        return True



main()