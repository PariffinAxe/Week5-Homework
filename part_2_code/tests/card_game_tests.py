import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.card1 = Card("Heart", 1)
        self.card2 = Card("Club", 6)
        self.card_game = CardGame()

    def test_check_ace_true(self):
        self.assertEquals(True, self.card_game.check_for_ace(self.card1))

    def test_check_ace_false(self):
        self.assertEquals(False, self.card_game.check_for_ace(self.card2))

    def test_highest_card(self):
        self.assertEquals(self.card2, self.card_game.highest_card(self.card1, self.card2))

    def test_cards_total(self):
        cards = [self.card1, self.card2]
        self.assertEquals("You have a total of 7", self.card_game.cards_total(cards))
