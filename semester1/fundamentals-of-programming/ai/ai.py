from point.point import Point
from board.board import ValidatePoint
from random import randint

class AI:

    def __init__(self, board):
        self.__board = board
        self.__valid = ValidatePoint()
        self.__startodd = False  #This tells us whether the AI is going to start on an odd board

    # GETTERS AND SETTERS

    def get_board(self):
        return self.__board

    def set_row(self, row):
        self.__board.set_row(row)

    def set_column(self, column):
        self.__board.set_column(column)

    # CREATE AND DESTROY BOARD

    def create_board(self):
        """This function creates the board and sets the __startodd variable to its default value"""
        self.__board.create_board()
        self.__startodd = False

    def destroy_board(self):
        """"This function destroys the board"""
        self.__board.destroy_board()

    #MOVES

    def make_move_player(self, x, y):
        """
        Function that validates the move the player wants to make.
        Raises exception if the move is invalid or if the square is unavailable,
        otherwise it records the move.
        """
        self.__valid.valid_point(x, y, self.__board)
        point = Point(x, y)
        self.__board.get_board()[point.get_x()][point.get_y()] = 1
        self.__board.board_move(point)

    def _check_odd(self, x, y):
        """"
        Function that return true if the board has an odd size
        and 0 otherwise
        """
        if x%2 == 1 or y%2 == 1:
            return 1
        else:
            return 0

    def _mirror_move(self, x, y):

        """"
        Function that mirrors the move the other player has made
        (Strategy used by the AI when it makes the first move on an od board)
        :param x: int - the coordinate that the player chose
        :param y: int - the coordinate that the player chose
        :returns: the mirror-point of the move made by the player
        """
        row = self.__board.get_row()
        col = self.__board.get_column()

        if self.__board.get_board()[row - x - 1][col - y - 1] == 0:
            return Point(row - x - 1, col - y - 1)

        if self.__board.get_board()[x][col - y - 1] == 0:
            return Point(x, col - y - 1)

        if self.__board.get_board()[row - x - 1][y] == 0:
            return Point(row - x - 1, y)

    def _random_move(self, moves):
        """Function that makes AI move randomly"""
        move = randint(0, len(moves) - 1)
        self.__board.get_board()[moves[move].get_x()][moves[move].get_y()] = 2
        self.__board.board_move(moves[move])
        return moves[move]

    def _decide_move(self, row, column, computer, moves):
        """"
        Function that decides the next move of the AI
        :param row: int, the number of rows in the board
        :param: column: int, the number of column in the board
        :param: computer: int, tells if the computer makes the first move
        :param: moves: the list of moves available
        :returns: 1 or 2
        """

        # If the AI starts we check if the board has odd coordinates
        if computer is True and len(moves) == row * column:
            if self._check_odd(row, column):
                return 1

        # If the board is odd and AI started we continue with 1
        if self.__startodd is True and len(moves) != row * column:
            return 1

        # If the above criteria wasn't met, the AI will just make its move randomly
        return 2

    def _first_odd(self, row, column, moves, x, y):
        """
        Function that follows the next strategy:
        If the board is odd and AI makes the first move, then the first move will be in the center of the board.
        In order to win, next the AI will only mirror the player's moves.
        """

        if row * column == len(moves):
            self.__board.get_board()[int(row//2)][int(column//2)] = 2
            self.__board.board_move(Point(int(row//2), int(column//2)))
            self.__startodd = True
            return Point(int(row//2), int(column//2))

        if row*column != len(moves):
            point = self._mirror_move(x, y)
            self.__board.get_board()[point.get_x()][point.get_y()] = 2
            self.__board.board_move(point)
            return point


    def make_move_ai(self, computer, x, y):
        """
        Function that makes the AI's move
        """

        moves = self.__board.available_moves()
        row = self.__board.get_row()
        column = self.__board.get_column()
        move = self._decide_move(row, column, computer, moves)

        if move == 1:
            return self._first_odd(row, column, moves, x, y)
        else:
            return self._random_move(moves)

    def game_over(self):
        """Function that returns True if there are still available moves to be made and False otherwise"""
        if self.__board.available_moves():
            return True
        return False









