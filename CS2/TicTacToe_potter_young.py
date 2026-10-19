import random

def main():
    playing = True

    p1_name = input('Enter a name for player 1: ')
    p2_name = input('Enter a name for player 2: ')

    print(f'{p1_name} choose a symbol!')
    while True:
        p1 = input('')
        if len(list(p1)) > 1:
            print('Please put a single character!')
        elif p1 == ' ' or p1 == '':
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
            elif p2 == p1:
                print('Please choose a unique character')
            else:
                break

    while True:

        board = [[' ', ' ' , ' '], 
                [' ', ' ', ' '], 
                [' ', ' ', ' ']]

        coinflip = random.randint(1,2)
        if coinflip == 1:
            print(f'{p1_name} ({p1}) is going first!')
        elif coinflip == 2:
            print(f'{p2_name} ({p2}) is going first!')
        else:
            print('something has gone horribly wrong')

        while playing == True:
            if coinflip == 1:
                result = player_turn(board, p1_name, p1)
                if result == True:
                    playing = False
                    continue

                result = player_turn(board, p2_name, p2) 
                if result == True:
                    playing = False
                    continue

            else:
                result = player_turn(board, p2_name, p2) 
                if result == True:
                    playing = False
                    continue

                result = player_turn(board, p1_name, p1)
                if result == True:
                    playing = False
                    continue
                
        print('Would you like to play again? (Y/N)')
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
    get_player_move(board, p_name, player)
    if check_winner(board, player) == True:
        print(f'{p_name} ({player}) has won!')
        return True
    elif is_draw(board) == True:
        print('Draw!')
        return True

def print_board(board):
    for row in range(2):
        print(f'{board[row][0]} | {board[row][1]} | {board[row][2]}')
        print('---------')
    print(f'{board[2][0]} | {board[2][1]} | {board[2][2]}')

def get_player_move(board, p_name, player):
    print(f'What tile do you want to fill, {p_name} ({player})?')

    while True:
        move = input('')

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
    for row in range(3):
        for column in range(3):
            if board[row][column] == ' ':
                return False
    return True

main()
