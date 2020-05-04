import unittest

from card import Card
from dealer import Dealer


class TestCanPlay(unittest.TestCase):

    def test_can_play_on_empty(self):
        """ Function coverage """
        dealer = Dealer()
        self.assertTrue(dealer.can_play())

    def test_can_play_under_limit(self):
        """ Branch coverage """
        dealer = Dealer()
        card1 = Card('Hearts', ('2', 2))
        card2 = Card('Hearts', ('3', 3))
        dealer.add_card(card1)
        dealer.add_card(card2)
        self.assertTrue(dealer.can_play())

    def test_can_play_over_limit(self):
        """ Branch coverage """
        dealer = Dealer()
        card1 = Card('Hearts', ('J', 10))
        card2 = Card('Hearts', ('3', 3))
        card3 = Card('Hearts', ('K', 10))
        dealer.add_card(card1)
        dealer.add_card(card2)
        dealer.add_card(card3)
        self.assertFalse(dealer.can_play())


if __name__ == '__main__':
    unittest.main()
