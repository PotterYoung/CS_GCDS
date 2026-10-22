'''
Name: Potter Young
Description: A game of Tic Tac Toe
Bugs: None known
Date: 10/21/26
Bonuses: Customizable symbol, Random turn order,
Log: Version 1.0: 10/21/26 
'''

import random

def main():

    playing = True                                                                  # Setting up a variable to track if a round is ongoing

    p1_name = input('Enter a name for player 1: ')                                  # Getting a name for each player
    p2_name = input('Enter a name for player 2: ')

    print(f'{p1_name} choose a symbol!')                                            # Letting the player choose a custom symbol
    while True:
        p1 = input('') 
        if len(list(p1)) > 1:                                                       # Checking if the symbol is longer than 1 character
            print('Please put a single character!')
        elif p1 == ' ' or p1 == '':                                                 # Checking if the symbol is empty or a space (both would break the game)
            print('Please input a valid character')
        else:
            break

    print(f'{p2_name} choose a symbol!')
    while True:
            p2 = input('')
            if len(list(p2)) > 1:
                print('Please put a single character!')
            elif p2 == ' ' or p2 == '':
                print('Please input a valid character')
            elif p2 == p1:                                                          # Checking if p2's symbol is the same as p1's
                print('Please choose a unique character')
            else:
                break

    while True:

        board = [[' ', ' ' , ' '],                                                  # Creating a blank 3x3 board to play on
                [' ', ' ', ' '], 
                [' ', ' ', ' ']]

        coinflip = random.randint(1,2)                                              # Random integer between 1-2 to see if p1 or p2 goes first
        if coinflip == 1:
            print(f'{p1_name} ({p1}) is going first!')
        elif coinflip == 2:
            print(f'{p2_name} ({p2}) is going first!')
        else:
            print('something has gone horribly wrong')

        while playing == True:
                                                                                    # Controlling the player turn order, getting specific player inputs, and getting out of the loop if the game is won/a draw
            if coinflip == 1:
                result = player_turn(board, p1_name, p1)
                if result == True:
                    playing = False
                    continue

                result = player_turn(board, p2_name, p2) 
                if result == True:
                    playing = False
                    continue

            else:                                                                   # If coin flipped 2, p2 goes before p1
                result = player_turn(board, p2_name, p2) 
                if result == True:
                    playing = False
                    continue

                result = player_turn(board, p1_name, p1)
                if result == True:
                    playing = False
                    continue
       
        print('Would you like to play again? (Y/N)')                                # Prompting the players to play again 
        while True:
            play_again = input('')
            if play_again.lower() == 'y':
                playing = True
                break
            elif play_again.lower() == 'n':
                quit()
            else:
                print('Invalid response')

def player_turn(board, p_name, player): 
    '''
    Calls the player move, and checks if the game is won/a draw
    Args:
        board (str): the board of play
        p_name (str): either p1 or p2's name
        player (str): either p1 or p2's symbol
    Return:
        Boolean: if the game is over or not
    '''
    get_player_move(board, p_name, player)                                          # Calling the player move function with the current player
    if check_winner(board, player) == True:                                         # Checking if the game is won/a draw
        print(f'{p_name} ({player}) has won!')
        return True
    elif is_draw(board) == True:
        print('Draw!')
        return True

def print_board(board):
    '''
    Prints out the board
    Args:
        board (str): the board of play
    Return:
        None
    '''
    for row in range(2):                                                            # Printing a horizontal line + the individual spots for every row (except the last)
        print(f'{board[row][0]} | {board[row][1]} | {board[row][2]}')
        print('---------')
    print(f'{board[2][0]} | {board[2][1]} | {board[2][2]}')                         # Hardcoded last line to not have another line

def get_player_move(board, p_name, player):
    '''
    Prompts the player for their move
    Args:
        board (str): the board of play
        p_name (str): either p1 or p2's name
        player (str): either p1 or p2's symbol
    Return:
        None
    '''
    print(f'What tile do you want to fill, {p_name} ({player})?')                   # Prompting the player for their move

    while True:
        move = input('')

                                                                                    # Checking if the spots the player chose are open, if so: filling them in, if not: asking them again
        if move == '1':
            if board[0][0] == ' ':
                board[0][0] = player
            else:
                print('That spot is taken')
                continue
        elif move == '2':
            if board[0][1] == ' ':
                board[0][1] = player
            else:
                print('That spot is taken')
                continue
        elif move == '3':
            if board[0][2] == ' ':
                board[0][2] = player
            else:
                print('That spot is taken')
                continue
        elif move == '4':
            if board[1][0] == ' ':
                board[1][0] = player
            else:
                print('That spot is taken')
                continue
        elif move == '5':
            if board[1][1] == ' ':
                board[1][1] = player
            else:
                print('That spot is taken')
                continue
        elif move == '6':
            if board[1][2] == ' ':
                board[1][2] = player
            else:
                print('That spot is taken')
                continue
        elif move == '7':
            if board[2][0] == ' ':
                board[2][0] = player
            else:
                print('That spot is taken')
                continue
        elif move == '8':
            if board[2][1] == ' ':
                board[2][1] = player
            else:
                print('That spot is taken')
                continue
        elif move == '9':
            if board[2][2] == ' ':
                board[2][2] = player
            else:
                print('That spot is taken')
                continue
        else:
            print('Invalid input')
            continue
        break
        
    print_board(board)

def check_winner(board, player):
    '''
    Checks if the current player has won
    Args:
        board (str): the board of play
        player (str): either p1 or p2's symbol
    Return:
        Boolean: If the game is won or not
    '''
                                                                                    # Checking all the win conditions and returning a boolean based on if any of them are met
    if board[0][0] == player and board[0][1] == player and board[0][2] == player:
        return True
    elif board[1][0] == player and board[1][1] == player and board[1][2] == player:
        return True
    elif board[2][0] == player and board[2][1] == player and board[2][2] == player:
        return True
    elif board[0][0] == player and board[1][0] == player and board[2][0] == player:
        return True
    elif board[0][1] == player and board[1][1] == player and board[2][1] == player:
        return True
    elif board[0][2] == player and board[1][2] == player and board[2][2] == player:
        return True
    elif board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    elif board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    else:
        return False

def is_draw(board):
    '''
    Checking if all spots are taken
    Args:
        board (str): the board of play
    Return:
        Boolean: If the game is a draw or not
    '''
                                                                                    # Checking if any spots are open, if not: returning that it is a draw, if so: returning that it is not a draw
    for row in range(3):
        for column in range(3):
            if board[row][column] == ' ':
                return False
    return True

main()