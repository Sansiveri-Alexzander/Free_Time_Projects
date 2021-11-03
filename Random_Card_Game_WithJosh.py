# Here is the game
# You have a deck of cards.
# You guess whether its going to be a red or black card
# You go through the entire deck and at the end it prints
# out how many you got right and how many you got wrong

# Steps
# create a deck of cards (52 cards, 2 to Ace for every suite)
# pop the cards one by one for each guess
import random
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
suites = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
red = ['Hearts', 'Diamonds']
black = ['Spades', 'Clubs']
color = [red, black]

deck = []

for value in values:
    for suite in suites:
        card = {
            'value': value,
            'suite': suite
        }
        deck.append(card)
# card -> value, suite ex: "Jack" "Spade"
# "Spade Clubs are black, and HEarts and Diamonds are Red"
random.shuffle(deck)

# loop through the deck
# while deck still has card
# pop the back card have the user quess
# record his correctness
# after the deck is empty print out the users score

c_answer = 0
w_answer = 0
num_red = 26
num_black = 26
num_card = 52

for x in range(0, 52):
    p_card = deck.pop()
    print('There is a', (int((num_red/num_card)*100)), '% chance of this card being red, and a',
          (int((num_black/num_card)*100)), '% chance of this card being black')
    color_guess = input("Guess if the cards color is red or black: ")
    print(p_card)
    # if color_guess != 'red' or 'black':
    #color_guess=input('Try again you must have mistyped ')
    if color_guess == 'red' and p_card['suite'] in red:
        print('correct')
        c_answer += 1
        num_red -= 1
        num_card -= 1
    elif color_guess == 'black' and p_card['suite'] in black:
        print('correct')
        c_answer += 1
        num_black -= 1
        num_card -= 1
    else:
        w_answer += 1
        if p_card['suite'] in red:
            num_red -= 1
        elif p_card['suite'] in black:
            num_black -= 1
        num_card -= 1
        print('wrong')
print("Correct: ", c_answer)
print("Wrong: ", w_answer)
# Have program guess the color
# have 8 decks being guessed
# run the program 1000 times and see what the best score was
