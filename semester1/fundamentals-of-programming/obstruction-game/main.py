from board.board import Board
from ai.ai import AI
from console.console import Console
from gui.gui import GUI

game = AI(Board())

ui = Console(game)
ui.start()

#ui = GUI(game)
