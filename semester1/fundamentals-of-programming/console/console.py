from board.board import Board
from ai.ai import AI
from random import randint

class Console:

    def __init__(self, ai_controller):
        self.__ai_controller = ai_controller
        self.__ai_start = False
        self.__in_turn = 1

    def start(self):
        print(" WELCOME TO THE OBSTRUCTION GAME!! :D ")
        choice = input("Do you wish to see the rules? :P  Or are you ready to play? ;) (rules/ ready) ---> ")
        if choice == 'rules' or choice == 'Rules' or choice == 'RULES':
            print("Ok so this is how this works:")
            print("There are two players: Me vs You")
            print("Each of us need to make moves on a board.")
            print("A move means writing your symbol in a cell from the board. By doing that, all the neighbors of that cell will be blocked")
            print("We play until the whole board is filled, and whoever makes the last move wins!")
            print("Good Luck! You will need it >:)")
        elif choice != 'ready':
            print("Well that was not an option.. I am just going to assume you are ready.")
        continue_game = True
        ok = 0
        print("Let's begin...")
        while continue_game:
            try:
                print("Please enter the size of the board:")
                x = int(input("Height -- > "))
                y = int(input("Length -- > "))
                if x<1 or y<1:
                    raise ValueError

                # Setting the size of the board
                self.__ai_controller.set_row(x)
                self.__ai_controller.set_column(y)
                self.__ai_controller.create_board()

                print("Who do you wish to start the game? 1 - you, 2 - the computer")
                choice = int(input("-- > "))
                if choice == 1:
                    self.__ai_start = False
                    self.__in_turn = 1
                elif choice == 2:
                    self.__ai_start = True
                    self.__in_turn = 2
                else:
                    print("ERROR! Invalid choice. Girly, it's between 1 or 2, come on.")
                    ok = 1
                    break

                while self.__ai_controller.game_over() is True:
                    if self.__in_turn == 1:
                        try:
                            print(str(self.__ai_controller.get_board()))
                            print("Time to enter your move! :D")
                            x = input("-- > x = ")
                            y = input("-- > y = ")
                            x = int(x)
                            y = int(y)
                            a = randint(0, 2)
                            if a == 0:
                                print("Alright then...my turn now!  >:)")
                            elif a == 1:
                                print("Ok! :P  My move will be: ")
                            elif a == 2:
                                print("HA! Let's see if you can beat this move :P")
                            self.__ai_controller.make_move_player(x, y)
                            self.__in_turn = 2
                        except Exception as error_lol:
                            print(error_lol)
                    elif self.__in_turn == 2:
                       self.__ai_controller.make_move_ai(self.__ai_start, x, y)
                       self.__in_turn = 1
                print(str(self.__ai_controller.get_board()))
                if self.__in_turn == 2:
                    print("Congrats, PLAYER has won! This time... >:)")
                else:
                    print("Computer has won!! :P")

                print("--> Do you wish to play again? 1 - yes, 0 - no")
                choice= int(input("-- > "))
                if choice == 1:
                    self.__ai_controller.destroy_board()
                elif choice == 0:
                    continue_game = False
                else:
                    print("Oops! Invalid choice :(")

            except ValueError:
                print("Oops! Invalid coordinates! :( Please try again!")

        if ok == 1:
            self.start()