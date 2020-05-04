from card import Card


class Player:

    def __init__(self, n='None'):
        self.__name = n
        self.hand = []

    def get_name(self):
        """
        Returns the name of the player.
        :return: str
        """
        return self.__name

    def add_card(self, card):
        """
        Adds the card to the player's hand if it is a Card object.
        :param card: Card
        :return: None
        """
        if isinstance(card, Card):
            self.hand.append(card)

    def get_player_points(self):
        """
        Gets the total amount of points in the player's hand. Handles aces with
        max and min totals. If the max total is greater than 21 and the min total is
        less than 21, it will return the min total. Otherwise it will return the max
        total.
        :return: int
        """
        min_total = 0
        max_total = 0

        for card in self.hand:
            point = card.get_point()
            min_total += point[1]
            max_total += 11 if point[0] == 'A' else point[1]

        return min_total if max_total > 21 else max_total
