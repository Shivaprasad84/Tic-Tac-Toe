import random

# Draw board
def display_board(board):
    print("\n"*100)
    print(" "*55 + '   |   |')
    print(" "*55 + ' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print(" "*55 + '   |   |')
    print(" "*55 + '-----------')
    print(" "*55 + '   |   |')
    print(" "*55 + ' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print(" "*55 + '   |   |')
    print(" "*55 + '-----------')
    print(" "*55 + '   |   |')
    print(" "*55 + ' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print(" "*55 + '   |   |')


# player input either X or O
def player_input():
    symbol = ''
    while not (symbol == 'X' or symbol == 'O'):
        symbol = input("Enter player1 symbol X or O: ").upper()
    if symbol == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


# Place marker at desired position
def place_marker(board, marker, position):
    board[position] = marker


# check for all possible winning combinations
def win_check(board, mark):
    if board[1] == mark and board[2] == mark and board[3] == mark:
        return True
    elif board[4] == mark and board[5] == mark and board[6] == mark:
        return True
    elif board[7] == mark and board[8] == mark and board[9] == mark:
        return True
    elif board[1] == mark and board[5] == mark and board[9] == mark:
        return True
    elif board[3] == mark and board[5] == mark and board[7] == mark:
        return True
    else:
        return False


# Choosing the first player using random library
def choose_first(player1, player2):
    return [player1, player2][random.randint(0,1)]


# Check if a cell is empty or not
def space_check(board, position):
    return board[position] == ' '


# Check if the board is full or not
def full_board_check(board):
    return ' ' not in board[1:-1]


# Position to place the marker
def player_choice(board):
    position = int(input("Enter position (1-9)"))
    if space_check(board, position):
        return position
    else:
        while not(space_check(board, position)):
            print("Position not empty")
            position = int(input("Enter position (1-9)"))
        return position


# Play again
def replay():
    choice = input("Do you want to play again?")
    if choice.lower() == 'yes':
        return True
    elif choice.lower() == 'no':
        return False


# Actual game
while True:
    print('Welcome to Tic Tac Toe!')
    board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    player1, player2 = player_input()
    if choose_first(player1, player2) == 'X':
        first_player, second_player = 'X', 'O'
    else:
        first_player, second_player = 'O', 'X'
        
    print(f'{first_player} will play first')
    while not full_board_check(board):
        # first_player
        pos = player_choice(board)
        place_marker(board, first_player, pos)
        display_board(board)
        if win_check(board, first_player):
            print(f'{first_player} wins!!!')
            break
        # second_player
        pos = player_choice(board)
        place_marker(board, second_player, pos)
        display_board(board)
        if win_check(board, second_player):
            print(f'{second_player} wins!!!')
            break
    
    if not replay():
        break
    
 