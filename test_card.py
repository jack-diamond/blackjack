import unittest

from card import Card


class TestGetSuit(unittest.TestCase):

    def test_suit(self):
        """ Function coverage """
        card = Card('Hearts', 2)
        self.assertEqual(card.get_suit(), 'Hearts')

    def test_suit_is_none(self):
        """ Edge coverage """
        card = Card()
        self.assertEqual(card.get_suit(), 'None')


class TestGetPoint(unittest.TestCase):

    def test_point(self):
        """ Function coverage """
        card = Card('Hearts', 2)
        self.assertEqual(card.get_point(), 2)

    def test_point_equal_zero(self):
        """ Edge coverage """
        card = Card()
        self.assertEqual(card.get_point(), 0)


class TestGetCardValue(unittest.TestCase):

    def test_value(self):
        """ Function coverage """
        card = Card('Hearts', 2)
        self.assertEqual(card.get_card_value(), '2 - Hearts')

    def test_value_empty_card(self):
        """ Edge coverage """
        card = Card()
        self.assertEqual(card.get_card_value(), '0 - None')


if __name__ == '__main__':
    unittest.main()
