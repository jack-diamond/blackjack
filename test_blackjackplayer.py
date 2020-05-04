import unittest

from blackjackplayer import BlackJackPlayer
from card import Card
from dealer import Dealer


class TestCanPlay(unittest.TestCase):

    def test_can_play_on_empty(self):
        """ Edge Case coverage """
        b_player = BlackJackPlayer()
        self.assertTrue(b_player.can_play())

    def test_can_play_under_limit(self):
        """ Function coverage """
        b_player = BlackJackPlayer()
        card1 = Card('Hearts', ('2', 2))
        card2 = Card('Hearts', ('3', 3))
        b_player.add_card(card1)
        b_player.add_card(card2)
        self.assertTrue(b_player.can_play())

    def test_can_play_over_limit(self):
        """ Function coverage """
        b_player = BlackJackPlayer()
        card1 = Card('Hearts', ('J', 10))
        card2 = Card('Hearts', ('3', 3))
        card3 = Card('Hearts', ('K', 10))
        b_player.add_card(card1)
        b_player.add_card(card2)
        b_player.add_card(card3)
        self.assertFalse(b_player.can_play())


class TestGetWantsToPlay(unittest.TestCase):

    def test_wants_is_true_after_constructor(self):
        """ Function coverage """
        b_player = BlackJackPlayer()
        self.assertTrue(b_player.get_wants_to_play())

    def test_wants_false_after_stop_playing(self):
        """ Function coverage """
        b_player = BlackJackPlayer()
        b_player.stop_playing()
        self.assertFalse(b_player.get_wants_to_play())


class TestStopPlaying(unittest.TestCase):

    def test_stop_playing_if_true(self):
        """ Function coverage """
        b_player = BlackJackPlayer()
        b_player.stop_playing()
        self.assertFalse(b_player.wants_to_play)

    def test_stop_playing_if_false(self):
        """ Edge Case """
        b_player = BlackJackPlayer()
        b_player.stop_playing()
        b_player.stop_playing()
        self.assertFalse(b_player.wants_to_play)


if __name__ == '__main__':
    unittest.main()
