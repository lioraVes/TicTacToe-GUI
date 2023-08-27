import tkinter as tk
from PIL import Image, ImageTk

ROOT_TITLE = "Welcome To Tic Tac Toe Game! :)"
ROOT_SIZE = "345x390"
ROOT_BG_COLOR = "#c691d5"
ROOT_BG_TAG = "bg"

TIC_PATH = "images/tic.png"
TAC_PATH = "images/tac.png"
TOE_PATH = "images/toe.png"

EXIT_BUTTON_TEXT = "Exit "

BUTTON_WIDTH = 15
BUTTON_HEIGHT = 5
NUM_BUTTONS_TOTAL = 9
BUTTON_PER_ROW = 3
HEADING_ROWS_NUM = 2
EXIT_ROW = 6
EXIT_COL = 1
SPACE_COL = 0
FIRST_SPACE_ROW = 1
SECOND_SPACE_ROW = 5


class Board:
    """ represent the TicTacToe board- with heading on top, 9 buttons and an
        exit button on the bottom. The buttons are without any logic """
    __root = tk.Tk()
    __buttons_arr = []
    __frame = tk.Frame(__root)

    def __init__(self):
        """ sets the board """
        self.__root.minsize(350, 395)
        self.set_heading()
        self.set_buttons()
        self.set_bottom()

        self.__frame.pack(expand=True, padx=5, pady=5)  # for responsive gui

    def get_root(self):
        """ a getter for the root """
        return self.__root

    def get_buttons_text_arr(self):
        """ a getter for the buttons content """
        lst = []
        for button in self.__buttons_arr:
            lst.append(button["text"])
        return lst

    def get_buttons_arr(self):
        """ a getter for the buttons"""
        return self.__buttons_arr

    def set_heading(self):
        """ sets the heading of the board """
        self.__root.title(ROOT_TITLE)
        self.__root.geometry(ROOT_SIZE)
        self.__root[ROOT_BG_TAG] = ROOT_BG_COLOR

        self.__frame[ROOT_BG_TAG] = ROOT_BG_COLOR

        paths = [TIC_PATH, TAC_PATH, TOE_PATH]

        for i in range(len(paths)):
            image = Image.open(paths[i])
            photo = ImageTk.PhotoImage(image)
            label = tk.Label(self.__frame, image=photo, bg=ROOT_BG_COLOR)
            label.image = photo
            label.grid(column=i, row=0)

        self.set_space(SPACE_COL, FIRST_SPACE_ROW)

    def set_space(self, col_num, row_num):
        """ creates a line of space on the board"""
        label = tk.Label(self.__frame, text="", bg=ROOT_BG_COLOR)
        label.grid(column=col_num, row=row_num)

    def set_buttons(self):
        """ creates the buttons """
        for i in range(NUM_BUTTONS_TOTAL):
            button = tk.Button(self.__frame, text="", width=BUTTON_WIDTH,
                               height=BUTTON_HEIGHT)
            row = (i // BUTTON_PER_ROW) + HEADING_ROWS_NUM
            col = i % BUTTON_PER_ROW
            button.grid(row=row, column=col)
            self.__buttons_arr.append(button)

    def set_bottom(self):
        """ creates the exit button """
        button12 = tk.Button(self.__frame, text=EXIT_BUTTON_TEXT,
                             width=BUTTON_WIDTH,
                             command=self.__root.destroy)
        button12.grid(column=EXIT_COL, row=EXIT_ROW)

        self.set_space(SPACE_COL, SECOND_SPACE_ROW)

    def reset_buttons(self):
        """resets the button content"""
        for button in self.__buttons_arr:
            button["text"] = ""

    def play(self):
        """start the gui"""
        self.__root.mainloop()
