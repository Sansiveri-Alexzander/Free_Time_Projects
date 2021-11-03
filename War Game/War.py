'''
Card
Suit, Rank, Value
'''

from random import shuffle

values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
          'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12,
          'King': 13, 'Ace': 14}
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine',
         'Ten', 'Jack', 'Queen', 'King', 'Ace')


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit

# two_hearts = Card("Hearts", "Two")
# print(two_hearts)


class Deck:
    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                # Create card object
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()


class Player:

    def __init__(self, name):

        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == list:
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return 'Player {} has {} cards.'.format(self.name, len(self.all_cards))

# Game Setup


player_one = Player("One")
player_two = Player("Two")

new_deck = Deck()
new_deck.shuffle()

for n in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

game_on = True

round_num = 0

while game_on:
    round_num += 1
    print("Round {}".format(round_num))

    if len(player_one.all_cards) == 0:
        print("Player 1 is out of cards! Player 2 wins")
        game_on = False
        break
    elif len(player_two.all_cards) == 0:
        print("Player 2 is out of cards! Player 1 wins")
        game_on = False
        break

    # Start a New Round
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())
    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    at_war = True

    # card check

    while at_war:
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            at_war = False
        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            at_war = False
        else:
            print("War!!!")

            if len(player_one.all_cards) < 4:
                print("Player 1 is unable to declare war")
                print("Player 2 Wins!")
                game_one = False
                break
            elif len(player_two.all_cards) < 4:
                print("Player 2 is unable to declare war")
                print("Player 1 Wins!")
                game_one = False
                break
            else:
                for num in range(4):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())
