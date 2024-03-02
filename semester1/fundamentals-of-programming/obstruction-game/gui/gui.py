from tkinter import *
from tkinter import messagebox
from gui.sixsixboard import SixSIxBoard
from gui.eighteightboard import EightEightBoard
from gui.seveneightboard import SevenEightBoard
from gui.sevennine import SevenNineBoard


class GUI:
    def __init__(self, ai):
        self.__ai = ai
        self.tk = Tk()
        self.tk.geometry("600x400+0+0")
        self.tk.title("Obstruction Game :D")

        # creating the frames:
        all_frames = Frame(self.tk)
        all_frames.pack()

        # creating the dictionary of frames, key = the class name of that frame
        self.frames = {}

        # Creating the starting frame:
        # This will contain the game title, the start game button, the exit button and info

        for frame in (StartGame, SixSIxBoard, EightEightBoard, SevenEightBoard, SevenNineBoard):
            fr = frame(all_frames, self, self.__ai)
            self.frames[frame] = fr
            fr.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartGame)

        self.tk.mainloop()

    def show_frame(self, name):
        """This function will show the current frame"""
        frame = name
        name = self.frames[name]
        if frame != StartGame:
            name.create_board()
            result = messagebox.askyesno("?", "Do you want to start the game?")
            if result is not True:
                name.first_ai()
        name.tkraise()

    def quit_frame(self):
        self.show_frame(StartGame)


class StartGame(Frame):
    def __init__(self, parent, controller, nothing):
        Frame.__init__(self, parent)
        self.game = ""
        self.__ctr = controller

        # Creating the title
        lblInfo = Label(self, font=('High Tower Text', 20, 'bold'), text="WELCOME to the Obstruction Game! :D", fg="#53166E", bd=20,
                        anchor='w')
        lblInfo.grid(row=0, column=0)

        # Adding a fill label to put a space between title and the next widgets
        fill_label = Label(self)
        fill_label.grid(row=1)

        # Creating the buttons for the game
        lbl = Label(self, font=('Jokerman', 15), text="Grid Sizes:", bd=1, anchor='e', fg="#703C86")
        lbl.grid(row=1, column=0)
        self.set(SixSIxBoard)

        # 3 radio buttons, one for each grid size
        radio_six = Radiobutton(self, text="6x6 BOARD", value=1, command=lambda: self.set(SixSIxBoard))
        radio_six.deselect()
        radio_six.grid(row=2)
        radio_seven = Radiobutton(self, text="7x8 BOARD", value=2, command=lambda: self.set(SevenEightBoard))
        radio_seven.deselect()
        radio_seven.grid(row=3)
        radio_eight = Radiobutton(self, text="7x9 BOARD", value=3, command=lambda: self.set(SevenNineBoard))
        radio_eight.grid(row=4)
        radio_eight.deselect()
        radio_eight = Radiobutton(self, text="8x8 BOARD", value=4, command=lambda: self.set(EightEightBoard))
        radio_eight.grid(row=5)
        radio_eight.deselect()

        # the buttons for start, description and quir
        self.start = Button(self, text="START", bg="#71DE7A", height=2, width=14, command=lambda: self.start_game())
        self.start.grid(row=7)
        self.desc = Button(self, text="DESCRIPTION", bg="#BC56C2", width=14, height=2, command=lambda: self.description())
        self.desc.grid(row=9)
        self.ButtonQuit = Button(self, background="#DA2C43", text="QUIT", height=2, width=14, command=lambda: Frame.quit(self))
        self.ButtonQuit.grid(row=11)

    def set(self, game_frame):
        self.game = game_frame

    @staticmethod
    def description():
        messagebox.showinfo("Description: ", "The Obstruction Game is played on a grid by two players; Player 1 is 'O' and the "
                                           "other one is 'X'. Players take turns in writing their symbol in a cell. By doing that, "
                                           " all the neighbors of that cell will become blocked. "
                                           "The restriction is that you can only make your move in a cell if all its neighbours are "
                                           "empty.The first player unable to move loses.")

    def start_game(self):
        self.__ctr.show_frame(self.game)
