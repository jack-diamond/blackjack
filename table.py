from blackjackplayer import BlackJackPlayer
from card import Card
from dealer import Dealer
from deck import Deck
from player import Player


class Table:

    def __init__(self, name='None'):
        self.player = BlackJackPlayer(name)
        self.dealer = Dealer('Oberyn')
        self.deck = Deck()
        self.deck.create_deck()
        self.deck.shuffle()
        self.hidden_card = None
        self.turns = []

    def play(self):
        """
        Gets the dealers hidden card and gives each player a card before starting the
        while loops to let the blackjackplayer take turns and the dealer to take turns.
        Stops looping if the player stands and if game ends.
        :return: None
        """
        self.hidden_card = self.deck.remove_card()

        self.give_card(self.dealer, self.deck.remove_card())
        self.give_card(self.player, self.deck.remove_card())

        while self.player.can_play() and self.player.get_wants_to_play() and not self.game_end():
            decision = input("Enter 'h' for hit or 's' for stand: ")
            if decision == 'h':
                self.give_card(self.player, self.deck.remove_card())
            elif decision == 's':
                self.player.stop_playing()
            else:
                print("Invalid input")

        if not self.game_end():
            self.give_card(self.dealer, self.hidden_card)
            while self.dealer.can_play() and not self.game_end():
                self.give_card(self.dealer, self.deck.remove_card())

        self.show_winner()

    def give_card(self, p: Player, c: Card):
        """
        Gives a card to the player, either dealer or blackjackplayer, and adds this to the table turns.
        :param p: Player, Dealer, or BlackJackPlayer
        :param c: Card
        :return: None
        """
        self.turns.append((p, c))
        p.add_card(c)
        print(p.get_name() + ' takes card ' + c.get_card_value() + ' for '
              + str(c.get_point()[1]) + '. Total = ' + str(p.get_player_points()))

    def game_end(self):
        """
        Returns true if either dealer or blackjackplayer is over or equal to 21.
        :return: bool
        """
        if self.player.get_player_points() >= 21:
            return True
        elif self.dealer.get_player_points() >= 21:
            return True
        return False

    def show_winner(self):
        """
        Prints which player has lost or won to the console, with their points.
        :return: None
        """
        if self.player.get_player_points() > 21:
            print(self.player.get_name() + ' has lost. ' + str(self.player.get_player_points()) + ' > 21')
        elif self.dealer.get_player_points() > 21:
            print(self.dealer.get_name() + ' has lost. ' + str(self.dealer.get_player_points()) + ' > 21')
        else:
            winner = self.player if self.player.get_player_points() > self.dealer.get_player_points() else self.dealer
            print(winner.get_name() + ' has won with ' + str(winner.get_player_points()) + ' points!')


if __name__ == '__main__':
    print("Version 1.2")
    name = input("Please enter your name... ")
    game = Table(name)
    print('Welcome to BlackJack. Your dealer will be Oberyn.')
    game.play()
