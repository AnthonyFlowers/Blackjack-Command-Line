# This class handles each action the dealer can preform
class Dealer:
    def __init__(self):
        self.hand = [] # List to store cards for the players hand
        self.name = 'Dealer'

    def dealCard(self, card):
        self.hand.append(card) # Add card from deck

    def calcHandValue(self):
        value = 0
        for card in self.hand:
            value += card.getValue()
        return value

    def showHand(self):
        print('----')
        value = 0
        print(self.name + ' has: ')
        if self.name != 'Dealer': # Handles the properly shown cards if its the dealer
            for card in self.hand:
                card.displayCard()
            print('With a value of: ' + str(self.calcHandValue()))
        else:
            print('One face down')
            self.hand[1].displayCard()

    def dealerShowHand(self):
        print('----')
        value = 0
        print(self.name + ' has: ')
        for card in self.hand:
            card.displayCard()
        print('With a value of: ' + str(self.calcHandValue()))


    def getName(self):
        return self.name
