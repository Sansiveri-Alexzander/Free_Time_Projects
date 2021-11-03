board = ['#', 1, 2, 3, 4, 5, 6, 7, 8, 9]
O = False
X = False
player2_choice = None
play_check = None


def display_board():  # function to display board
    print('|', board[1], '|', board[2], '|', board[3], '|')
    print('|', board[4], '|', board[5], '|', board[6], '|')
    print('|', board[7], '|', board[8], '|', board[9], '|')


def player_input():  # determines player 1's input (either X or O)
    player1_choice = input("Player 1: Would you like to be X or O: ").upper()
    while player1_choice not in ['X', 'O']:
        player1_choice = input("Player 1: Try again. Please input either 'X' or 'O': ").upper()
    if player1_choice == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


def player2_input():  # determines player 2's input
    if player1_choice == 'X':
        player2_choice = 'O'
    elif player1_choice == 'O':
        player2_choice = 'X'
    return player2_choice


def placement_player1():  # determines where player1 wants to go
    if player1_choice == 'X':
        placementP1 = input('Player 1: Where would you like to place your X (1-9):')
    elif player1_choice == 'O':
        placementP1 = input('Player 1: Where would you like to place your O (1-9):')
    return placementP1


def placement_player2():  # determines where player1 wants to go
    if player2_choice == 'X':
        placementP2 = input('Player 2: Where would you like to place your X (1-9):')
    elif player2_choice == 'O':
        placementP2 = input('Player 2: Where would you like to place your O (1-9):')
    return placementP2


# checks if the placement is valid and sends a message which can be interpreted by the placement_change() function
def placement_check(placement):
    try:
        val = int(placement)
    except ValueError:
        return 1
    else:
        if int(placement) not in list(range(1, 10)):
            return 2
        elif board[int(placement)] in ['X', 'O']:
            return 3
        else:
            return 4


# takes in the new input having been reported an error with the initial placement choice
def placement_change(placement):
    if placement_check(placement) == 1:  # anything other than a number
        print('Not an Integer!!!')
        placement = input('Invalid Input. Please input a NUMBER between 1 and 9: ')
        return placement
    elif placement_check(placement) == 2:  # Spot not in list range
        placement = input("This spot doesn't exist on the board. Try again: ")
        return placement
    elif placement_check(placement) == 3:  # Spot is taken by an X or an O
        placement = input('This spot is taken. Please try again: ')
        return placement
    elif placement_check(placement) == 4:  # input is valid
        return placement


def board_replacement(place, choice):  # replace player's choice with desired symbol
    # try:
        #board[int(place)] = choice
    # except ValueError:
        #print('Not an integer!')
    # else:
    board[int(place)] = choice


def checkGame_Over():  # checks if the game is over
    # if board[1,3] or board[6,9]
    for num in range(1, 10):
        if num in board:
            return False
        else:
            continue
    print('Tie Game')
    return True


def GameWinner_Check(O_winner, X_winner):  # checks if P1 or P2 has won the game
    if (board[1] == board[2] == board[3] == 'X'):
        X_winner = True
    elif board[1] == board[5] == board[9] == 'X':
        X_winner = True
    elif board[1] == board[4] == board[7] == 'X':
        X_winner = True
    elif board[3] == board[6] == board[9] == 'X':
        X_winner = True
    elif board[3] == board[5] == board[7] == 'X':
        X_winner = True
    elif board[4] == board[5] == board[6] == 'X':
        X_winner = True
    elif board[7] == board[8] == board[9] == 'X':
        X_winner = True
    elif board[2] == board[5] == board[8] == 'X':
        X_winner = True
    elif board[1] == board[2] == board[3] == 'O':
        O_winner = True
    elif board[1] == board[5] == board[9] == 'O':
        O_winner = True
    elif board[1] == board[4] == board[7] == 'O':
        O_winner = True
    elif board[3] == board[6] == board[9] == 'O':
        O_winner = True
    elif board[3] == board[5] == board[7] == 'O':
        O_winner = True
    elif board[4] == board[5] == board[6] == 'O':
        O_winner = True
    elif board[7] == board[8] == board[9] == 'O':
        O_winner = True
    elif board[2] == board[5] == board[8] == 'O':
        O_winner = True
    if O_winner:
        if player1_choice == 'O':
            print('Player 1 Has Won!!!')
            return True
        elif player2_choice == 'O':
            print('Player 2 Has Won!!!')
            return True
    elif X_winner:
        if player1_choice == 'X':
            print('Player 1 Has Won!!!')
            return True
        elif player2_choice == 'X':
            print('Player 2 Has Won!!!')
            return True


def PlayAgain_Check():  # checks if the player wants to play again
    play_check = input('Would you like to play again? (Y or N): ').upper()
    while play_check not in ['Y', 'N']:
        play_check = input(
            'Invalid Input. Would you like to play again? Please choose(Y or N): ').upper()
    if play_check == 'Y':
        return True
    if play_check == 'N':
        return False


# Code for the Game to run


while True:  # play again loop
    board = ['#', 1, 2, 3, 4, 5, 6, 7, 8, 9]
    player1_choice, player2_choice = player_input()
    display_board()
    while True:  # game loop
        if player1_choice == 'O':  # Player 2 Goes first
            placementP2 = placement_player2()
            while placement_check(placementP2) in [1, 2, 3]:  # Waits until valid input is given
                placementP2 = placement_change(placementP2)
            board_replacement(placementP2, player2_choice)
            display_board()
            if GameWinner_Check(O, X):
                break
            elif checkGame_Over():
                break
            placementP1 = placement_player1()
            while placement_check(placementP1) in [1, 2, 3]:  # Waits until valid input is given
                placementP1 = placement_change(placementP1)
            board_replacement(placementP1, player1_choice)
            display_board()
            if GameWinner_Check(O, X):
                break
        else:  # Player 1 goes first
            placementP1 = placement_player1()
            while placement_check(placementP1) in [1, 2, 3]:  # Waits until valid input is given
                placementP1 = placement_change(placementP1)
            board_replacement(placementP1, player1_choice)
            display_board()
            if GameWinner_Check(O, X):
                break
            elif checkGame_Over():
                break
            placementP2 = placement_player2()
            while placement_check(placementP2) in [1, 2, 3]:  # Waits until valid input is given
                placementP2 = placement_change(placementP2)
            board_replacement(placementP2, player2_choice)
            display_board()
            if GameWinner_Check(O, X):
                break
    if PlayAgain_Check():
        continue
    else:
        break


print('End Game')
