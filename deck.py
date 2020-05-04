from card import Card
import random


class Deck:

    def __init__(self):
        self.cards = []
        self.suits = ['Hearts', 'Spades', 'Clubs', 'Diamonds']
        self.points = [('A', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5), ('6', 6), ('7', 7),
                       ('8', 8), ('9', 9), ('10', 10), ('J', 10), ('Q', 10), ('K', 10)]

    def create_deck(self):
        """
        Creates a deck from the above suits and points by making a Card with
        each value and appending it to the cards array.
        :return: None
        """
        for s in self.suits:
            for p in self.points:
                self.cards.append(Card(s, p))

    def shuffle(self):
        """
        Utilizes Python's built in shuffle function to shuffle the Card objects order
        within the cards array.
        :return: None
        """
        random.shuffle(self.cards)

    def remove_card(self):
        """
        Removes the top card from the cards array (greatest index) if the length
        of the cards array > 0, else it prints an error and returns None.
        :return: Card, None
        """
        if len(self.cards) == 0:
            print('No more cards!')
            return
        top_card = self.cards.pop()
        return top_card
