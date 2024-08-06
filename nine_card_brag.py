import random

# Creating a player class
# This will store how many points / rounds won and the cards the player holds etc.
class Player:
    
    def __init__ (self, name, money = 100, bet_amount = 0, cards = None, round_points = 0, games_won = 0, games_lost = 0):
        self.name = name
        self.money = money
        self.bet_amount = bet_amount
        self.cards = cards or []
        self.round_points = round_points
        self.games_won = games_won
        self.games_lost = games_lost
    
    def __repr__ (self):
        return 'Hello {name}. You have £{money}. Games won: {rounds_won}. Games lost: {rounds_lost}.'.format(name = self.name, money = self.money, rounds_won = self.games_won, rounds_lost = self.games_lost)


# information needed in cards deck is value and suit
# if multiple players then need to store amount of each card
# each deck has four of each value in each suit
# once card has been assigned to player, it cant be played again

class Cards:

    cards_in_deck = {'Ace':4, 'Two':4, 'Three':4, 'Four':4, 'Five':4, 'Six':4, 'Seven':4, 'Eight':4, 'Nine':4, 'Ten':4, 'Jack':4, 'Queen':4, 'King':4}
    card_suits = ['Spades', 'Clubs', 'Hearts', 'Diamonds']

    def __init__(self, decks, card_amount, cards_played = {}):
        self.decks = decks
        self.card_amount = {key: value * decks for key, value in Cards.cards_in_deck.items()}
        self.cards_played = cards_played

new_player = Player('Dave')
print(new_player)
