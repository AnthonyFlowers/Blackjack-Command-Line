import unittest
from blackjack import blackjack
# from blackjack import BlackjackGame, Dealer, Player, Card, Deck
from unittest.mock import Mock, patch

class TestGameClass(unittest.TestCase):

    ### Test creating blackjack game ###
    def test_create_game_1(self):
        game = blackjack.BlackjackGame(1, 100, ['Anthony'])
        self.assertEqual(game.playerAmount, 1)
        self.assertEqual(game.chipCount, 100)
        self.assertEqual(game.playerNames[0], 'Anthony')

    def test_create_game_2(self):
        game = blackjack.BlackjackGame(1, 150, ['John'])
        self.assertEqual(game.playerAmount, 1)
        self.assertEqual(game.chipCount, 150)
        self.assertEqual(game.playerNames[0], 'John')

    def test_create_game_3(self):
        game = blackjack.BlackjackGame(1, 400, ['Sean'])
        self.assertEqual(game.playerAmount, 1)
        self.assertEqual(game.chipCount, 400)
        self.assertEqual(game.playerNames[0], 'Sean')


    ### Test creating cards ###
    def test_create_card(self):
        card = blackjack.Card(10, 1)
        self.assertEqual(card.displayCard(), '10 of Spades')
        self.assertEqual(card.getValue(), 10)
        self.assertFalse(card.isAce)

    def test_create_card(self):
        card = blackjack.Card(1, 2)
        self.assertEqual(card.displayCard(), 'Ace of Clubs')
        self.assertTrue(card.isAce)
        self.assertEqual(card.getValue(), 11)

    def test_create_card(self):
        card = blackjack.Card(3, 3)
        self.assertEqual(card.displayCard(), '3 of Diamonds')
        self.assertEqual(card.getValue(), 3)
        self.assertFalse(card.isAce)

    def test_create_card(self):
        card = blackjack.Card(13, 4)
        self.assertEqual(card.displayCard(), 'King of Hearts')
        self.assertEqual(card.getValue(), 10)
        self.assertFalse(card.isAce)

    ### Test deck methods ###
    def test_create_deck(self):
        deck = blackjack.Deck()
        deck.deck.append(blackjack.Card(8, 1))
        deck.deck.append(blackjack.Card(2, 3))
        self.assertEqual(len(deck.deck), 2)
        self.assertEqual(deck.drawCard().displayCard(), blackjack.Card(2, 3).displayCard())
        self.assertEqual(len(deck.deck), 1)
        self.assertEqual(deck.drawCard().displayCard(), blackjack.Card(8, 1).displayCard())
        self.assertEqual(len(deck.deck), 0)
        deck.deck.append(blackjack.Card(9, 4))

    def test_create_full_deck(self):
        full_deck = blackjack.Deck()
        full_deck.createDeck()
        self.assertEqual(len(full_deck.deck), 52)
        full_deck.drawCard()
        full_deck.shuffleDeck()
        self.assertEqual(len(full_deck.deck), 51)
        full_deck.clear()
        self.assertEqual(len(full_deck.deck), 0)

    ### Test file IO ###
    def test_setting_chips_file_1(self):
        blackjack.setChipsFile('Test Name 1', 125, 'tests\\test_chips.txt')
        with open('tests\\test_chips.txt', 'r') as chip_file:
            info = chip_file.read().split(':')
            self.assertEqual(info[0], 'Test Name 1')
            self.assertEqual(int(blackjack.getStartChips('tests\\test_chips.txt')), 125)

    def test_setting_chips_file_2(self):
        blackjack.setChipsFile('Test Name 2', 400, 'tests\\test_chips.txt')
        with open('tests\\test_chips.txt', 'r') as chip_file:
            info = chip_file.read().split(':')
            self.assertEqual(info[0], 'Test Name 2')
            self.assertEqual(int(blackjack.getStartChips('tests\\test_chips.txt')), 400)

    ### Test player and dealer class ###
    def test_player_class(self):
        player = blackjack.Player(100, 'Anthony')
        self.assertEqual(player.chips, 100)
        self.assertEqual(player.name, 'Anthony')
        self.assertEqual(len(player.hand), 0)
        player.dealCard(blackjack.Card(5, 3))
        player.dealCard(blackjack.Card(3, 1))
        self.assertEqual(player.calcHandValue(), 8)
        player.dealCard(blackjack.Card(7, 2))
        self.assertEqual(player.calcHandValue(), 15)

    def test_dealer_class(self):
        dealer = blackjack.Dealer()
        dealer.dealCard(blackjack.Card(8, 1))
        dealer.dealCard(blackjack.Card(1, 4))
        self.assertEqual(dealer.calcHandValue(), 19)
        dealer.dealCard(blackjack.Card(3, 1))
        self.assertEqual(dealer.calcHandValue(), 22)

    ### Test game logic ###
    def test_game_logic(self):
        # Start values
        player_number = 1
        player_chips = 100

        # Create game and initialize player
        game = blackjack.BlackjackGame(player_number, player_chips, ['Anthony'])
        game.initializePlayers(player_number, player_chips)

        # Create some cards
        card1 = blackjack.Card(10, 3)
        card2 = blackjack.Card(8, 1)
        card3 = blackjack.Card(13, 2)
        card4 = blackjack.Card(3, 4)

        # Deal some predetermined cards
        game.playerList[0].dealCard(card1)
        game.dealer.dealCard(card2)
        game.playerList[0].dealCard(card3)
        game.dealer.dealCard(card4)

        # Test hand values
        player_hand_value = game.playerList[0].calcHandValue()
        dealer_hand_value = game.dealer.calcHandValue()
        self.assertEqual(player_hand_value, 20)
        self.assertEqual(dealer_hand_value, 11)
