from player import Player


class Dealer(Player):

    def __init__(self, n='None'):
        super().__init__(n)

    def can_play(self):
        """
        Determines if the player can still keep playing. According to rules,
        the dealer will only play if their score is less than 17.
        :return: bool
        """
        return self.get_player_points() <= 16
