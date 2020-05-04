class Card:

    def __init__(self, s='None', p=0):
        self.__suit = s
        self.__point = p

    def get_suit(self):
        """
        Returns the suit of the card.
        :return: str
        """
        return self.__suit
    
    def get_point(self):
        """
        Returns the point of the card in a tuple containing the type (1,2,J,K)
        and its point value.
        :return: tuple
        """
        return self.__point

    def get_card_value(self):
        """
        Displays the value of the card.
        :return: None
        """
        return str(self.get_point()) + ' - ' + self.get_suit()
