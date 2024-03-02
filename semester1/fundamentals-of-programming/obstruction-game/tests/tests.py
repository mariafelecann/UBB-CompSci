from ai.ai import AI
import unittest
import random
from board.board import Board


class test_board(unittest.TestCase):

    def test_create_board(self):
        """"
        Tests the function create_board from Board
        """
        boardd = Board(3, 3)
        aii = AI(boardd)
        boardd.create_board()
        self.assertEqual(len(boardd._board[0]), 3)
        self.assertEqual(boardd._board[0][0], 0)

    def test_available_moves(self):
        """"
        Tests the available_moves from Board
        """
        boardd = Board(3, 3)
        aii = AI(boardd)
        boardd.create_board()
        moves = boardd.available_moves()
        self.assertEqual(len(moves), 9)

    def test_make_move_player(self):
        """"
        Tests the function make_move_player from AI
        """
        boardd = Board(3, 3)
        aii = AI(boardd)
        boardd.create_board()
        aii.make_move_player(0, 0)
        self.assertEqual(boardd._board[0][0], 1)

    def test_decide_move(self):
        """"
        Tests the function decide_move from AI
        """
        boardd = Board(3, 3)
        aii = AI(boardd)
        boardd.create_board()
        aii._decide_move(0, 1, 0, boardd.available_moves())
        self.assertEqual(boardd._board[0][1], 0)

    def test_destroy_board(self):
        """"
        Tests the function destroy_board from AI
        """
        boardd = Board(3, 3)
        aii = AI(boardd)
        boardd.create_board()
        aii.destroy_board()
        self.assertEqual(boardd.get_board(), [])

if __name__ == '__main__':
    unittest.main()