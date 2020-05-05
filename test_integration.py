import unittest

from blackjackplayer import BlackJackPlayer
from card import Card
from dealer import Dealer
from player import Player
from table import Table


class TestIntegration(unittest.TestCase):

    def test_give_card_player(self):
        """
        Ensure that the Player and Table components work together by
        having the teable give the player a card from the deck.
        :return: None
        """
        player = Player('Jack')
        card = Card('Hearts', ('2', 2))
        table = Table()
        table.give_card(player, card)
        suit = player.hand[0].get_suit()
        point = player.hand[0].get_point()
        pair = (suit, point)
        self.assertEqual(pair, ('Hearts', ('2', 2)))

    def test_give_card_dealer(self):
        """
        Ensure that the inheritance works for Player/Dealer and the Table
        component can give the player the right card.
        :return: None
        """
        player = Dealer('Jack')
        card = Card('Hearts', ('2', 2))
        table = Table()
        table.give_card(player, card)
        suit = player.hand[0].get_suit()
        point = player.hand[0].get_point()
        pair = (suit, point)
        self.assertEqual(pair, ('Hearts', ('2', 2)))

    def test_give_card_blackjackplayer(self):
        """
        Ensure the inheritance between Blackjackplayer/Player works and
        the table gives the player the correct card.
        :return: None
        """
        player = BlackJackPlayer('Jack')
        card = Card('Hearts', ('2', 2))
        table = Table()
        table.give_card(player, card)
        suit = player.hand[0].get_suit()
        point = player.hand[0].get_point()
        pair = (suit, point)
        self.assertEqual(pair, ('Hearts', ('2', 2)))

    def test_game_end_player_over_21(self):
        """
        Ensure that the table and player class work together
        and the table verifies that the player has over 21 points.
        :return: None
        """
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
        """
        Test whether or not the game is over with an Ace card which
        can be counted as 1 or 11. In this case it should be over.
        :return: None
        """
        player = Player()
        card2 = Card('Hearts', ('J', 10))
        card3 = Card('Hearts', ('A', 1))
        table = Table()
        table.give_card(player, card2)
        table.give_card(player, card3)
        table.player = player
        self.assertTrue(table.game_end())

    def test_game_end_player_under_21_with_ace(self):
        """
        Testing whether or not the game ends with an Ace card when the
        total score is under 21.
        :return: None
        """
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
        """
        Simulate the hit command from the user. Verify that the table
        gives the correct cards to the players.
        :return: None
        """
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
        """
        Simulate a scenario when the player stands but the dealer goes over
        21 resulting in the player winning the game.
        :return: None
        """
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
        """
        Simulates a scenario where the player stands but the dealer is below 21.
        The game should not be over.
        :return: None
        """
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
