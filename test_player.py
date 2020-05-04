import unittest

from card import Card
from player import Player


class TestGetName(unittest.TestCase):

    def test_name_is_equal_string(self):
        """ Function coverage """
        name = 'Jack'
        player = Player(name)
        self.assertEqual(player.get_name(), 'Jack')

    def test_name_is_equal_none(self):
        """ Edge coverage """
        player = Player()
        self.assertEqual(player.get_name(), 'None')


class TestAddCard(unittest.TestCase):

    def test_add_card(self):
        """ Function coverage """
        card = Card('Hearts', ('A', 1))
        player = Player()
        player.add_card(card)
        self.assertEqual(player.hand[0], card)

    def test_add_invalid_card(self):
        """ Edge coverage """
        player = Player()
        player.add_card('1')
        self.assertEqual(len(player.hand), 0)


class TestGetPlayerPoints(unittest.TestCase):

    def test_get_points_one_card(self):
        """ Function coverage """
        card = Card('Hearts', ('2', 2))
        player = Player()
        player.add_card(card)
        self.assertEqual(player.get_player_points(), 2)

    def test_get_points_two_cards(self):
        """ Function coverage """
        card1 = Card('Hearts', ('2', 2))
        card2 = Card('Hearts', ('3', 3))
        player = Player()
        player.add_card(card1)
        player.add_card(card2)
        self.assertEqual(player.get_player_points(), 5)

    def test_get_points_ace_card_min_total(self):
        """ Branch coverage """
        card1 = Card('Hearts', ('Q', 10))
        card2 = Card('Diamonds', ('A', 1))
        card3 = Card('Hearts', ('2', 2))
        player = Player()
        player.add_card(card1)
        player.add_card(card2)
        player.add_card(card3)
        self.assertEqual(player.get_player_points(), 13)

    def test_get_points_ace_card_max_total(self):
        """ Branch coverage """
        card1 = Card('Hearts', ('Q', 10))
        card2 = Card('Diamonds', ('A', 1))
        player = Player()
        player.add_card(card1)
        player.add_card(card2)
        self.assertEqual(player.get_player_points(), 21)


if __name__ == '__main__':
    unittest.main()
