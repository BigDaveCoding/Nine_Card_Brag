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


new_player = Player('Dave')
print(new_player)
