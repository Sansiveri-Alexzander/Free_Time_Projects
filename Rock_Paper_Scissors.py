'''
first rock paper scissor shoot game
quite poorly made with only two definitions
--- the whole game and the end of the game ---
'''

# Importing the random module

import random

# Creating list and setting games won to 0

print("Let's play a game of 'Rock Paper Scissors' best out of three!")
alist = ['rock', 'paper', 'scissors']
w_games = 0

# Def of the whole game


def rpsgame():
    user_input = "Y"
    global w_games
    while user_input != "Q":
        game = 0
        score = 0
        while game != 3:
            print(score)
            answer = input(str("Rock, Paper, Scissors Shoot: "))
            ai_1 = random.choice(alist)
            if answer == "rock":
                if ai_1 == "rock":
                    print(ai_1.upper())
                    print("We Tied")
                    game += 1
                elif ai_1 == "scissors":
                    print(ai_1.upper())
                    print('You Win')
                    score += 1
                    game += 1
                else:
                    print(ai_1.upper())
                    print('You Lose')
                    score -= 1
                    game += 1
            elif answer == "paper":
                if ai_1 == "paper":
                    print(ai_1.upper())
                    print("We Tied")
                    game += 1
                elif ai_1 == "rock":
                    print(ai_1.upper())
                    print('You Win')
                    score += 1
                    game += 1
                else:
                    print(ai_1.upper())
                    print('You Lose')
                    score -= 1
                    game += 1
            else:
                if ai_1 == "scissors":
                    print(ai_1.upper())
                    print("We Tied")
                    game += 1
                elif ai_1 == "paper":
                    print(ai_1.upper())
                    print('You Win')
                    score += 1
                    game += 1
                else:
                    print(ai_1.upper())
                    print('You Lose')
                    score -= 1
                    game += 1
        if score > 0:
            print('Congrats you won the best of three games against me.')
            w_games += 1
        elif score < 0:
            print('Aw Shucks seems like you have lost to me out of three games. Better luck next time.')
            w_games -= 1
        else:
            while score == 0:
                print(score)
                answer = input(str("Rock, Paper, Scissors Shoot: "))
                ai_1 = random.choice(alist)
                if answer == "rock":
                    if ai_1 == "rock":
                        print(ai_1.upper())
                        print("We Tied")
                        game += 1
                    elif ai_1 == "scissors":
                        print(ai_1.upper())
                        print('You Win')
                        score += 1
                        game += 1
                    else:
                        print(ai_1.upper())
                        print('You Lose')
                        score -= 1
                        game += 1
                elif answer == "paper":
                    if ai_1 == "paper":
                        print(ai_1.upper())
                        print("We Tied")
                        game += 1
                    elif ai_1 == "rock":
                        print(ai_1.upper())
                        print('You Win')
                        score += 1
                        game += 1
                    else:
                        print(ai_1.upper())
                        print('You Lose')
                        score -= 1
                        game += 1
                else:
                    if ai_1 == "scissors":
                        print(ai_1.upper())
                        print("We Tied")
                        game += 1
                    elif ai_1 == "paper":
                        print(ai_1.upper())
                        print('You Win')
                        score += 1
                        game += 1
                    else:
                        print(ai_1.upper())
                        print('You Lose')
                        score -= 1
                        game += 1
            if score > 0:
                print('Close game, well played')
                w_games += 1
            elif score < 0:
                print('Close game, Better luck next time lad')
                w_games -= 1

        user_input = input('If you wish to play another game (Type Y) if you wish to quit (type Q)')


rpsgame()

# Telling user how many games they won/lost


def endgame():
    print('Have a good day sire')
    if w_games == 1:
        print('You won', w_games, 'game')
    elif w_games == -1:
        print('You lost', abs(w_games), 'game')
    elif w_games > 0:
        print('You won a total of', w_games, 'games')
    elif w_games < 0:
        print('You lost a total of', abs(w_games), 'games')
    else:
        print('You won and lost the same amount of games against me')


endgame()
