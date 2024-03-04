from board.board import Board
from ai.ai import AI
from console.console import Console


game = AI(Board())

ui = Console(game)
ui.start()

