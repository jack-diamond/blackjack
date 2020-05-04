import unittest

from deck import Deck


class TestCreateDeck(unittest.TestCase):

    def test_create_deck_size(self):
        """ Function coverage """
        deck = Deck()
        deck.create_deck()
        valid_deck_size = 52
        self.assertEqual(len(deck.cards), valid_deck_size)

    def test_create_deck_values(self):
        """ Function coverage """
        deck = Deck()
        deck.create_deck()
        values = [('A', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5), ('6', 6), ('7', 7),
                  ('8', 8), ('9', 9), ('10', 10), ('J', 10), ('Q', 10), ('K', 10),
                  ('A', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5), ('6', 6), ('7', 7),
                  ('8', 8), ('9', 9), ('10', 10), ('J', 10), ('Q', 10), ('K', 10),
                  ('A', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5), ('6', 6), ('7', 7),
                  ('8', 8), ('9', 9), ('10', 10), ('J', 10), ('Q', 10), ('K', 10),
                  ('A', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5), ('6', 6), ('7', 7),
                  ('8', 8), ('9', 9), ('10', 10), ('J', 10), ('Q', 10), ('K', 10)]
        verify = []
        for card in deck.cards:
            verify.append(card.get_point())
        self.assertEqual(verify, values)

    def test_create_deck_suits_hearts(self):
        """ Function coverage """
        deck = Deck()
        deck.create_deck()
        d = {'Hearts': 0}
        for card in deck.cards:
            if card.get_suit() in d:
                d[card.get_suit()] += 1
        self.assertEqual(d['Hearts'], 13)

    def test_create_deck_suits_spades(self):
        """ Function coverage """
        deck = Deck()
        deck.create_deck()
        d = {'Spades': 0}
        for card in deck.cards:
            if card.get_suit() in d:
                d[card.get_suit()] += 1
        self.assertEqual(d['Spades'], 13)

    def test_create_deck_suits_clubs(self):
        """ Function coverage """
        deck = Deck()
        deck.create_deck()
        d = {'Clubs': 0}
        for card in deck.cards:
            if card.get_suit() in d:
                d[card.get_suit()] += 1
        self.assertEqual(d['Clubs'], 13)

    def test_create_deck_suits_diamonds(self):
        """ Function coverage """
        deck = Deck()
        deck.create_deck()
        d = {'Diamonds': 0}
        for card in deck.cards:
            if card.get_suit() in d:
                d[card.get_suit()] += 1
        self.assertEqual(d['Diamonds'], 13)


class TestShuffle(unittest.TestCase):

    def test_shuffle_before_shuffled(self):
        """ Function coverage """
        deck = Deck()
        deck.create_deck()
        before = []
        for card in deck.cards:
            before.append(card.get_point())
        deck.shuffle()
        after = []
        for card in deck.cards:
            after.append(card.get_point())
        self.assertNotEqual(before, after)

    def test_shuffle_after_shuffled(self):
        """ Function, Edge coverage """
        deck = Deck()
        deck.create_deck()
        deck.shuffle()
        before = []
        for card in deck.cards:
            before.append(card.get_point())
        deck.shuffle()
        after = []
        for card in deck.cards:
            after.append(card.get_point())
        self.assertNotEqual(before, after)


class TestRemoveCard(unittest.TestCase):

    def test_remove_card(self):
        """ Function coverage """
        deck = Deck()
        deck.create_deck()
        values = []
        for card in deck.cards:
            values.append(card.get_point())
        before = values[-1]
        after = deck.remove_card().get_point()
        self.assertEqual(before, after)

    def test_remove_card_on_empty(self):
        """ Edge coverage """
        deck = Deck()
        self.assertEqual(deck.remove_card(), None)


if __name__ == '__main__':
    unittest.main()
