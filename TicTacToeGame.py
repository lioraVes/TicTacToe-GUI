from Board import Board
from tkinter import messagebox
from Player import Player

TEXT_BUTTONS_PROPERTY = "text"
NUM_PLAYERS = 2
MESSAGE_BOX_TITLE = "TIC TAC TOE"
ILLEGAL_MOVE_MSG = "Illegal move !"
NUM_BUTTONS_TOTAL = 9
NUM_BUTTONS_PER_ROW = 3
NO_WIN_MSG = "Game Over-No One Won"
FIRST_PLAYER_MARK = "X"
SECOND_PLAYER_MARK = "O"
GAME_OVER_MSG = "Game Over, would you like to play again?"
FIRST_PLAYER_IND = 0
SECOND_PLAYER_IND = 1


class TicTacToeGame:
    """ manages a TicTacToe Game """

    def __init__(self, game_board, player1, player2):
        self.board = game_board
        self.set_buttons_logic()
        self.players_arr = [player1, player2]
        self.cur_player = 0
        self.marked_buttons = 0
        self.winner = False
        self.start_player = 0

    def set_buttons_logic(self):
        """sets the buttons logic"""
        buttons_arr = self.board.get_buttons_arr()
        for button in buttons_arr:
            button.config(command=lambda b=button: self.click(b))

    def click(self, button):
        """ the function that is going to be executed when the player clicks
        on a button """
        if button[TEXT_BUTTONS_PROPERTY] == "":
            self.players_arr[self.cur_player].put_mark(button)
            self.marked_buttons += 1
            self.cur_player = (self.cur_player + 1) % NUM_PLAYERS
        else:
            # clicking on marked button
            messagebox.showerror(MESSAGE_BOX_TITLE, ILLEGAL_MOVE_MSG)

        self.check_winner()

    def check_winner(self):
        """ checks for a winner"""
        buttons_text_arr = self.board.get_buttons_text_arr()
        if self.check_row_win(buttons_text_arr) or \
                self.check_col_win(buttons_text_arr) or \
                self.check_diagonal_win(buttons_text_arr):
            self.end_game()
        else:
            # no one won
            if self.marked_buttons == NUM_BUTTONS_TOTAL and \
                    self.winner is False:
                messagebox.showinfo(MESSAGE_BOX_TITLE, NO_WIN_MSG)
                self.end_game()

    def check_row_win(self, lst):
        """ check if there is a row winner """
        for i in range(0, NUM_BUTTONS_TOTAL, NUM_BUTTONS_PER_ROW):
            if lst[i] == lst[i + 1] == lst[i + 2] and lst[i] != "":
                self.winner = True
                messagebox.showinfo(MESSAGE_BOX_TITLE, "Player " + lst[i] +
                                    " Won-Row")
                if lst[i] == FIRST_PLAYER_MARK:
                    self.players_arr[FIRST_PLAYER_IND].add_point()
                else:
                    self.players_arr[SECOND_PLAYER_IND].add_point()
                return True

    def check_col_win(self, lst):
        """ check if there is a col winner """
        for i in range(NUM_BUTTONS_PER_ROW):
            if lst[i] == lst[i + 3] == lst[i + 6] and lst[i] != "":
                self.winner = True
                messagebox.showinfo(MESSAGE_BOX_TITLE,
                                    "Player " + lst[i] + " Won-Column")
                if lst[i] == FIRST_PLAYER_MARK:
                    self.players_arr[FIRST_PLAYER_IND].add_point()
                else:
                    self.players_arr[SECOND_PLAYER_IND].add_point()
                return True

    def check_diagonal_win(self, lst):
        """ check if there is a diagonal winner """
        if (lst[0] == lst[4] == lst[8]) and (lst[0] != ""):
            self.winner = True
            messagebox.showinfo(MESSAGE_BOX_TITLE, "Player " +
                                lst[0] + " Won-Diagonal")
            if ((lst[0] == lst[4] == lst[8]) and (
                    lst[0] == FIRST_PLAYER_MARK)):
                self.players_arr[FIRST_PLAYER_IND].add_point()
            else:
                self.players_arr[SECOND_PLAYER_IND].add_point()
            return True

        elif (lst[2] == lst[4] == lst[6]) and (lst[2] != ""):
            self.winner = True
            messagebox.showinfo(MESSAGE_BOX_TITLE, "Player " +
                                lst[2] + " Won-Diagonal")
            if (lst[2] == lst[4] == lst[6]) and (lst[2] == FIRST_PLAYER_MARK):
                self.players_arr[FIRST_PLAYER_IND].add_point()
            else:
                self.players_arr[SECOND_PLAYER_IND].add_point()
            return True

    def end_game(self):
        """handles the end of the game"""
        msg = messagebox.askyesno(MESSAGE_BOX_TITLE, GAME_OVER_MSG)
        if not msg:
            X_win = self.players_arr[FIRST_PLAYER_IND].get_player_score()
            O_win = self.players_arr[SECOND_PLAYER_IND].get_player_score()
            overall_win = ""
            if X_win == O_win:
                overall_win = "tie"
            elif X_win > O_win:
                overall_win = "X"
            else:
                overall_win = "O"

            messagebox.showinfo(MESSAGE_BOX_TITLE,
                                "Player X Won " + str(X_win) + " times\n"
                                + "Player O Won " + str(O_win) + " times\n" +
                                "Overall winner is: " + overall_win)
            self.board.get_root().destroy()
        else:
            self.reset_game()
            self.play()

    def reset_game(self):
        """ resets the game board for a new game"""
        self.start_player = 1 - self.start_player
        if (
                self.cur_player != self.start_player): self.cur_player = self.start_player
        self.marked_buttons = 0
        self.winner = False
        self.board.reset_buttons()

    def play(self):
        """ this function starts the game"""
        self.board.play()


if __name__ == "__main__":
    board = Board()
    playerX = Player(FIRST_PLAYER_MARK)
    playerO = Player(SECOND_PLAYER_MARK)
    game = TicTacToeGame(board, playerX, playerO)
    game.play()
