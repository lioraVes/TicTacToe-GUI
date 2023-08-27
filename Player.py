BUTTON_TEXT_PROPERTY = "text"


class Player:
    """ represents a player """
    def __init__(self, player_mark):
        self.mark = player_mark
        self.score = 0

    def put_mark(self, button):
        """ puts the players mark in the given button"""
        button[BUTTON_TEXT_PROPERTY] = self.mark

    def add_point(self):
        """add a point to the player score"""
        self.score += 1

    def get_player_score(self):
        """ a getter for the player score"""
        return self.score
