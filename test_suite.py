import unittest
import test_dealer
import test_player
import test_blackjackplayer
import test_card
import test_deck

def create_suite():
    loader = unittest.TestLoader()
    test_suite = unittest.TestSuite()
    test_suite.addTest(loader.loadTestsFromModule(test_dealer))
    test_suite.addTest(loader.loadTestsFromModule(test_blackjackplayer))
    test_suite.addTest(loader.loadTestsFromModule(test_player))
    test_suite.addTest(loader.loadTestsFromModule(test_card))
    test_suite.addTest(loader.loadTestsFromModule(test_deck))
    return test_suite


if __name__ == '__main__':
    suite = create_suite()

    runner = unittest.TextTestRunner()
    runner.run(suite)
