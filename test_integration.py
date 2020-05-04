import unittest

from blackjackplayer import BlackJackPlayer
from card import Card
from dealer import Dealer
from player import Player
from table import Table


class TestIntegration(unittest.TestCase):

    def test_give_card_player(self):
        player = Player('Jack')
        card = Card('Hearts', ('2', 2))
        table = Table()
        table.give_card(player, card)
        suit = player.hand[0].get_suit()
        point = player.hand[0].get_point()
        pair = (suit, point)
        self.assertEqual(pair, ('Hearts', ('2', 2)))

    def test_give_card_dealer(self):
        player = Dealer('Jack')
        card = Card('Hearts', ('2', 2))
        table = Table()
        table.give_card(player, card)
        suit = player.hand[0].get_suit()
        point = player.hand[0].get_point()
        pair = (suit, point)
        self.assertEqual(pair, ('Hearts', ('2', 2)))

    def test_give_card_blackjackplayer(self):
        player = BlackJackPlayer('Jack')
        card = Card('Hearts', ('2', 2))
        table = Table()
        table.give_card(player, card)
        suit = player.hand[0].get_suit()
        point = player.hand[0].get_point()
        pair = (suit, point)
        self.assertEqual(pair, ('Hearts', ('2', 2)))

    def test_game_end_player_over_21(self):
        player = Player()
        card1 = Card('Hearts', ('K', 10))
        card2 = Card('Hearts', ('J', 10))
        card3 = Card('Hearts', ('10', 10))
        table = Table()
        table.give_card(player, card1)
        table.give_card(player, card2)
        table.give_card(player, card3)
        table.player = player
        self.assertTrue(table.game_end())

    def test_game_end_player_equals_21_with_ace(self):
        player = Player()
        card2 = Card('Hearts', ('J', 10))
        card3 = Card('Hearts', ('A', 1))
        table = Table()
        table.give_card(player, card2)
        table.give_card(player, card3)
        table.player = player
        self.assertTrue(table.game_end())

    def test_game_end_player_under_21_with_ace(self):
        player = Player()
        card2 = Card('Hearts', ('9', 9))
        card3 = Card('Hearts', ('A', 1))
        table = Table()
        table.give_card(player, card2)
        table.give_card(player, card3)
        table.player = player
        self.assertFalse(table.game_end())

    def test_game_end_dealer_over_21(self):
        player = Player()
        card1 = Card('Hearts', ('K', 10))
        card2 = Card('Hearts', ('J', 10))
        card3 = Card('Hearts', ('10', 10))
        table = Table()
        table.give_card(player, card1)
        table.give_card(player, card2)
        table.give_card(player, card3)
        table.player = player
        self.assertTrue(table.game_end())

    def test_player_hits(self):
        player = Player()
        card1 = Card('Hearts', ('2', 2))
        card2 = Card('Diamonds', ('10', 10))
        table = Table()
        table.give_card(player, card1)
        table.give_card(player, card2)
        table.player = player
        suit = table.player.hand[0].get_suit()
        point = table.player.hand[0].get_point()
        pair1 = (suit, point)
        suit = table.player.hand[1].get_suit()
        point = table.player.hand[1].get_point()
        pair2 = (suit, point)
        pairs = [pair1, pair2]
        self.assertEqual(pairs, [('Hearts', ('2', 2)), ('Diamonds', ('10', 10))])

    def test_player_stands_and_dealer_loses(self):
        player = BlackJackPlayer()
        dealer = Dealer()
        card1 = Card('Hearts', ('K', 10))
        card2 = Card('Hearts', ('J', 10))
        card3 = Card('Hearts', ('3', 3))
        table = Table()
        table.give_card(player, card1)
        table.give_card(player, card2)
        table.player = player
        self.assertFalse(table.game_end())
        table.give_card(dealer, card1)
        table.give_card(dealer, card2)
        table.give_card(dealer, card3)
        table.dealer = dealer
        self.assertTrue(table.game_end())

    def test_player_stands_and_dealer_is_below_21(self):
        player = BlackJackPlayer()
        dealer = Dealer()
        card1 = Card('Hearts', ('K', 10))
        card2 = Card('Hearts', ('9', 9))
        card3 = Card('Hearts', ('1', 1))
        table = Table()
        table.give_card(player, card1)
        table.give_card(player, card2)
        table.player = player
        self.assertFalse(table.game_end())
        table.give_card(dealer, card1)
        table.give_card(dealer, card2)
        table.give_card(dealer, card3)
        table.dealer = dealer
        self.assertFalse(table.game_end())


if __name__ == '__main__':
    unittest.main()
