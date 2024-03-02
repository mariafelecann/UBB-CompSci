from point.point import Point

class Board:

    def __init__(self, row=0, column=0):
        self.__row = row
        self.__column = column
        self._board = []

    # GETTERS AND SETTERS

    def get_board(self):
        return self._board

    def get_row(self):
        return self.__row

    def get_column(self):
        return self.__column

    def set_row(self, row):
        self.__row = row

    def set_column(self, column):
        self.__column = column

    # CREATE AND DESTROY

    def destroy_board(self):
        """"
        This function destroys the board
        """
        self.__row = 0
        self.__column = 0
        self._board = []

    def create_board(self):
        """"
        This function creates the board
        """
        arr = []

        for i in range(self.__row):
            for j in range(self.__column):
                arr.append(0)
            self._board.append(arr)
            arr = []

    # MOVES

    def available_moves(self):
        """"
        This function returnes the available moves the current player can make
        :return: moves
        """
        moves = []
        for i in range(self.get_row()):
            for j in range(self.get_column()):
                if self._board[i][j] == 0:
                    pointy = Point(i, j)
                    moves.append(pointy)

        return moves

    def board_move(self, point):
        """"
        This function boards the move of the current player
        :param point: member of Point class, has the coordonates of the current move
        :return: None
        """

        x = point.get_x()
        y = point.get_y()

        if x - 1 >= 0 and y - 1 >= 0 and self._board[x - 1][y - 1] == 0:
            self._board[x - 1][y - 1] = -1
        if x - 1 >= 0 and self._board[x - 1][y] == 0:
            self._board[x - 1][y] = -1
        if x - 1 >= 0 and y + 1 < self.__column and self._board[x - 1][y + 1] == 0:
            self._board[x - 1][y + 1] = -1
        if y - 1 >= 0 and self._board[x][y - 1] == 0:
            self._board[x][y - 1] = -1
        if y + 1 < self.__column and self._board[x][y + 1] == 0:
            self._board[x][y + 1] = -1
        if x + 1 < self.__row and y + 1 < self.__column and self._board[x + 1][y + 1] == 0:
            self._board[x + 1][y + 1] = -1
        if x + 1 < self.__row and self._board[x + 1][y] == 0:
            self._board[x + 1][y] = -1
        if x + 1 < self.__row and y - 1 >= 0 and self._board[x + 1][y - 1] == 0:
            self._board[x + 1][y - 1] = -1

    # OVERRIDING FUNCTIONS

    def __len__(self):

        return len(self._board)

    def __str__(self):
        """
        Redefining the str function so the board is printed
        :param: string: a string containing the board
        :return: string
        """

        string = "\n   "
        for x in range(self.__column):
            string += str(x) + '   '
        for x in range(self.__row):
            string += "\n "
            string += "-" * (4 * self.__column + 1)
            string += "\n"
            string += str(x) + '|'
            for y in range(self.__column):
                if self._board[x][y] == 1:  # 1 = the player
                    string += ' ' + '0' + ' ' + "|"
                elif self._board[x][y] == 2:  # 2 = the computer
                    string += ' ' + 'X' + ' ' + "|"
                elif self._board[x][y] == -1:  # -1 = nonempty neighbours
                    string += '@@ ' + "|"
                else:
                    string += ' ' + ' ' + ' ' + "|"
        string += "\n "
        string += "-" * (4 * self.__column + 1) + "\n"
        return string

class ValidatePoint:
    @staticmethod

    def valid_point(x, y, board):
        """Function that validates the coordinates of a point given"""
        try:
            x = int(x)
            y = int(y)
        except ValueError:
            raise Exception("Please give integers! (just pick integers girly, you can do this!)")
        if y < 0 or x < 0 or y >= board.get_column() or x >= board.get_row():
            raise Exception("Point out of border! (girl, you chose the height and length...cmon)")
        if board.get_board()[x][y] == -1 or board.get_board()[x][y] == 1 or board.get_board()[x][y] == 2:
            raise Exception("Square already taken!(girl, choose from the empty spaces, there are plenty...)")