from .dealer import Dealer
# This class handles each action a player can do and the information stored for each player
class Player (Dealer):
    def __init__(self, playerChips, playerName):
        self.chips = playerChips
        self.name = playerName
        self.hand = [] # List to store cards for the players hand
    pass
