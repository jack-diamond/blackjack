from player import Player


class BlackJackPlayer(Player):

    def __init__(self, n='None'):
        super().__init__(n)
        self.wants_to_play = True

    def can_play(self):
        """
        Returns true if the player points are below 21, else false.
        :return: bool
        """
        return self.get_player_points() < 21

    def get_wants_to_play(self):
        """
        Returns the boolean value of wants_to_play.
        :return: bool
        """
        return self.wants_to_play

    def stop_playing(self):
        """
        Sets wants_to_play to false when the player stands.
        :return: None
        """
        self.wants_to_play = False
