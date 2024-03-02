from tkinter import *
from tkinter import messagebox


class SevenEightBoard(Frame):
    def __init__(self, parent, controller, ai):
        Frame.__init__(self, parent)
        self.__ai = ai
        self.__ctr = controller
        self.in_turn = 1  # Variable that keeps track of who is going to make the move next
        self.destroy = 0  # Variable that saves if the user wants to quit the frame or not
        self.first = 0

        """ROW 0"""
        self.Button1 = Button(self, activebackground="#d9d9d9", activeforeground="#341a87", background="#e1ccd5",
                              disabledforeground="#ffe5e5", foreground="#341a87", highlightcolor="black", relief=SUNKEN,
                              height=2, width=5, pady="0", padx="0",
                              command=lambda: self.make_move(0, 0, self.Button1, self.Button2, self.Button8, self.Button7))
        self.Button1.grid(row=0, column=0)

        self.Button2 = Button(self, activebackground="#d9d9d9", activeforeground="#341a87", background="#e1ccd5",
                              disabledforeground="#ffe5e5", foreground="#341a87", highlightcolor="black", relief=SUNKEN,
                              height=2, width=5, pady="0", padx="0",
                              command=lambda: self.make_move(0, 1, self.Button2, self.Button1, self.Button3,
                                                             self.Button7, self.Button8, self.Button9))
        self.Button2.grid(row=0, column=1)

        self.Button3 = Button(self, activebackground="#d9d9d9", activeforeground="#341a87", background="#e1ccd5",
                              disabledforeground="#ffe5e5", foreground="#341a87", highlightcolor="black", relief=SUNKEN,
                              height=2, width=5, pady="0", padx="0",
                              command=lambda: self.make_move(0, 2, self.Button3, self.Button2, self.Button8,
                                                             self.Button4, self.Button9, self.Button10))
        self.Button3.grid(row=0, column=2)

        self.Button4 = Button(self, activebackground="#d9d9d9", activeforeground="#341a87", background="#e1ccd5",
                              disabledforeground="#ffe5e5", foreground="#341a87", highlightcolor="black", relief=SUNKEN,
                              height=2, width=5, pady="0", padx="0",
                              command=lambda: self.make_move(0, 3, self.Button4, self.Button5, self.Button3,
                                                             self.Button9, self.Button10, self.Button11))
        self.Button4.grid(row=0, column=3)

        self.Button5 = Button(self, activebackground="#d9d9d9", activeforeground="#341a87", background="#e1ccd5",
                              disabledforeground="#ffe5e5", foreground="#341a87", highlightcolor="black", relief=SUNKEN,
                              height=2, width=5, pady="0", padx="0",
                              command=lambda: self.make_move(0, 4, self.Button5, self.Button6, self.Button10,
                                                             self.Button4, self.Button11, self.Button12))
        self.Button5.grid(row=0, column=4)

        self.Button6 = Button(self, activebackground="#d9d9d9", activeforeground="#341a87", background="#e1ccd5",
                              disabledforeground="#ffe5e5", foreground="#341a87", highlightcolor="black", relief=SUNKEN,
                              height=2, width=5, pady="0", padx="0",
                              command=lambda: self.make_move(0, 5, self.Button6, self.Button5, self.Button11,
                                                             self.Button12, self.Button_seven, self.Button_thirteen))
        self.Button6.grid(row=0, column=5)

        self.Button_seven = Button(self, activebackground="#d9d9d9", activeforeground="#341a87", background="#e1ccd5",
                              disabledforeground="#ffe5e5", foreground="#341a87", highlightcolor="black", relief=SUNKEN,
                              height=2, width=5, pady="0", padx="0",
                              command=lambda: self.make_move(0, 6, self.Button_seven, self.Button_eight,
                                                             self.Button6, self.Button12, self.Button_thirteen,
                                                             self.Button_fourteen))
        self.Button_seven.grid(row=0, column=6)

        self.Button_eight = Button(self, activebackground="#d9d9d9", activeforeground="#341a87", background="#e1ccd5",
                              disabledforeground="#ffe5e5", foreground="#341a87", highlightcolor="black", relief=SUNKEN,
                              height=2, width=5, pady="0", padx="0",
                              command=lambda: self.make_move(0, 7, self.Button_eight, self.Button_seven,
                                                             self.Button_thirteen, self.Button_fourteen))
        self.Button_eight.grid(row=0, column=7)

        """ ROW 1"""
        self.Button7 = Button(self, activebackground="#d9d9d9", activeforeground="#341a87", background="#e1ccd5",
                              disabledforeground="#ffe5e5", foreground="#341a87", highlightcolor="black", relief=SUNKEN,
                              height=2, width=5, pady="0", padx="0",
                              command=lambda: self.make_move(1, 0, self.Button7, self.Button1, self.Button2,
                                                             self.Button8, self.Button13, self.Button14))
        self.Button7.grid(row=1, column=0)

        self.Button8 = Button(self, activebackground="#d9d9d9", activeforeground="#341a87", background="#e1ccd5",
                              disabledforeground="#ffe5e5", foreground="#341a87", highlightcolor="black", relief=SUNKEN,
                              height=2, width=5, pady="0", padx="0",
                              command=lambda: self.make_move(1, 1, self.Button8, self.Button1, self.Button3,
                                                             self.Button7, self.Button2, self.Button9,
                                                             self.Button13, self.Button14, self.Button15))
        self.Button8.grid(row=1, column=1)

        self.Button9 = Button(self, activebackground="#d9d9d9", activeforeground="#341a87", background="#e1ccd5",
                              disabledforeground="#ffe5e5", foreground="#341a87", highlightcolor="black", relief=SUNKEN,
                              height=2, width=5, pady="0", padx="0",
                              command=lambda: self.make_move(1, 2, self.Button9, self.Button2, self.Button8,
                                                             self.Button4, self.Button3, self.Button10,
                                                             self.Button16, self.Button14, self.Button15))
        self.Button9.grid(row=1, column=2)

        self.Button10 = Button(self, activebackground="#d9d9d9", activeforeground="#341a87", background="#e1ccd5",
                              disabledforeground="#ffe5e5", foreground="#341a87", highlightcolor="black", relief=SUNKEN,
                              height=2, width=5, pady="0", padx="0",
                              command=lambda: self.make_move(1, 3, self.Button10, self.Button5, self.Button3,
                                                             self.Button9, self.Button4, self.Button11,
                                                             self.Button16, self.Button17, self.Button15))
        self.Button10.grid(row=1, column=3)

        self.Button11 = Button(self, activebackground="#d9d9d9", activeforeground="#341a87", background="#e1ccd5",
                              disabledforeground="#ffe5e5", foreground="#341a87", highlightcolor="black", relief=SUNKEN,
                              height=2, width=5, pady="0", padx="0",
                              command=lambda: self.make_move(1, 4, self.Button11, self.Button6, self.Button10,
                                                             self.Button4, self.Button5, self.Button12,
                                                             self.Button16, self.Button17, self.Button18))
        self.Button11.grid(row=1, column=4)

        self.Button12 = Button(self, activebackground="#d9d9d9", activeforeground="#341a87", background="#e1ccd5",
                              disabledforeground="#ffe5e5", foreground="#341a87", highlightcolor="black", relief=SUNKEN,
                              height=2, width=5, pady="0", padx="0",
                              command=lambda: self.make_move(1, 5, self.Button12, self.Button5, self.Button11,
                                                             self.Button6, self.Button17, self.Button18,
                                                             self.Button_seven, self.Button_thirteen, self.Button_nineteen))
        self.Button12.grid(row=1, column=5)

        self.Button_thirteen = Button(self, activebackground="#d9d9d9", activeforeground="#341a87", background="#e1ccd5",
                               disabledforeground="#ffe5e5", foreground="#341a87", highlightcolor="black",
                               relief=SUNKEN,
                               height=2, width=5, pady="0", padx="0",
                               command=lambda: self.make_move(1, 6, self.Button_thirteen, self.Button_seven, self.Button12,
                                                              self.Button6, self.Button18, self.Button_eight,
                                                              self.Button_nineteen, self.Button_fourteen, self.Button_twenty))
        self.Button_thirteen.grid(row=1, column=6)

        self.Button_fourteen = Button(self, activebackground="#d9d9d9", activeforeground="#341a87", background="#e1ccd5",
                               disabledforeground="#ffe5e5", foreground="#341a87", highlightcolor="black",
                               relief=SUNKEN,
                               height=2, width=5, pady="0", padx="0",
                               command=lambda: self.make_move(1, 7, self.Button_fourteen, self.Button_seven,
                                                              self.Button_eight, self.Button_thirteen,
                                                              self.Button_nineteen, self.Button_twenty))
        self.Button_fourteen.grid(row=1, column=7)

        """ROW 2"""

        self.Button13 = Button(self, activebackground="#d9d9d9", activeforeground="#341a87", background="#e1ccd5",
                              disabledforeground="#ffe5e5", foreground="#341a87", highlightcolor="black", relief=SUNKEN,
                              height=2, width=5, pady="0", padx="0",
                              command=lambda: self.make_move(2, 0, self.Button13, self.Button19, self.Button20,
                                                             self.Button8, self.Button7, self.Button14))
        self.Button13.grid(row=2, column=0)

        self.Button14 = Button(self, activebackground="#d9d9d9", activeforeground="#341a87", background="#e1ccd5",
                              disabledforeground="#ffe5e5", foreground="#341a87", highlightcolor="black", relief=SUNKEN,
                              height=2, width=5, pady="0", padx="0",
                              command=lambda: self.make_move(2, 1, self.Button14, self.Button19, self.Button21,
                                                             self.Button7, self.Button20, self.Button9,
                                                             self.Button13, self.Button8, self.Button15))
        self.Button14.grid(row=2, column=1)

        self.Button15 = Button(self, activebackground="#d9d9d9", activeforeground="#341a87", background="#e1ccd5",
                              disabledforeground="#ffe5e5", foreground="#341a87", highlightcolor="black", relief=SUNKEN,
                              height=2, width=5, pady="0", padx="0",
                              command=lambda: self.make_move(2, 2, self.Button15, self.Button20, self.Button8,
                                                             self.Button21, self.Button22, self.Button10,
                                                             self.Button16, self.Button14, self.Button9))
        self.Button15.grid(row=2, column=2)

        self.Button16 = Button(self, activebackground="#d9d9d9", activeforeground="#341a87", background="#e1ccd5",
                               disabledforeground="#ffe5e5", foreground="#341a87", highlightcolor="black",
                               relief=SUNKEN,
                               height=2, width=5, pady="0", padx="0",
                               command=lambda: self.make_move(2, 3, self.Button16, self.Button21, self.Button22,
                                                              self.Button9, self.Button23, self.Button11,
                                                              self.Button10, self.Button17, self.Button15))
        self.Button16.grid(row=2, column=3)

        self.Button17 = Button(self, activebackground="#d9d9d9", activeforeground="#341a87", background="#e1ccd5",
                               disabledforeground="#ffe5e5", foreground="#341a87", highlightcolor="black",
                               relief=SUNKEN,
                               height=2, width=5, pady="0", padx="0",
                               command=lambda: self.make_move(2, 4, self.Button17, self.Button22, self.Button10,
                                                              self.Button24, self.Button23, self.Button12,
                                                              self.Button16, self.Button11, self.Button18))
        self.Button17.grid(row=2, column=4)

        self.Button18 = Button(self, activebackground="#d9d9d9", activeforeground="#341a87", background="#e1ccd5",
                               disabledforeground="#ffe5e5", foreground="#341a87", highlightcolor="black",
                               relief=SUNKEN,
                               height=2, width=5, pady="0", padx="0",
                               command=lambda: self.make_move(2, 5, self.Button18, self.Button23, self.Button11,
                                                              self.Button24, self.Button17, self.Button12,
                                                              self.Button_thirteen, self.Button_nineteen,
                                                              self.Button_twentyfive))
        self.Button18.grid(row=2, column=5)

        self.Button_nineteen = Button(self, activebackground="#d9d9d9", activeforeground="#341a87", background="#e1ccd5",
                               disabledforeground="#ffe5e5", foreground="#341a87", highlightcolor="black",
                               relief=SUNKEN,
                               height=2, width=5, pady="0", padx="0",
                               command=lambda: self.make_move(2, 6, self.Button_nineteen, self.Button_thirteen,
                                                              self.Button24, self.Button12, self.Button18,
                                                              self.Button_twentyfive, self.Button_fourteen,
                                                              self.Button_twenty, self.Button_twentysix))
        self.Button_nineteen.grid(row=2, column=6)

        self.Button_twenty = Button(self, activebackground="#d9d9d9", activeforeground="#341a87", background="#e1ccd5",
                               disabledforeground="#ffe5e5", foreground="#341a87", highlightcolor="black",
                               relief=SUNKEN,
                               height=2, width=5, pady="0", padx="0",
                               command=lambda: self.make_move(2, 7, self.Button_twenty, self.Button_nineteen,
                                                              self.Button_twentyfive, self.Button_fourteen,
                                                              self.Button_thirteen, self.Button_twentysix))
        self.Button_twenty.grid(row=2, column=7)

        """ROW 3"""

        self.Button19 = Button(self, activebackground="#d9d9d9", activeforeground="#341a87", background="#e1ccd5",
                               disabledforeground="#ffe5e5", foreground="#341a87", highlightcolor="black",
                               relief=SUNKEN,
                               height=2, width=5, pady="0", padx="0",
                               command=lambda: self.make_move(3, 0, self.Button19, self.Button13, self.Button20,
                                                              self.Button25, self.Button26, self.Button14))
        self.Button19.grid(row=3, column=0)

        self.Button20 = Button(self, activebackground="#d9d9d9", activeforeground="#341a87", background="#e1ccd5",
                               disabledforeground="#ffe5e5", foreground="#341a87", highlightcolor="black",
                               relief=SUNKEN,
                               height=2, width=5, pady="0", padx="0",
                               command=lambda: self.make_move(3, 1, self.Button20, self.Button19, self.Button21,
                                                              self.Button25, self.Button14, self.Button26,
                                                              self.Button13, self.Button27, self.Button15))
        self.Button20.grid(row=3, column=1)

        self.Button21 = Button(self, activebackground="#d9d9d9", activeforeground="#341a87", background="#e1ccd5",
                               disabledforeground="#ffe5e5", foreground="#341a87", highlightcolor="black",
                               relief=SUNKEN,
                               height=2, width=5, pady="0", padx="0",
                               command=lambda: self.make_move(3, 2, self.Button21, self.Button20, self.Button26,
                                                              self.Button15, self.Button22, self.Button28,
                                                              self.Button16, self.Button14, self.Button27))
        self.Button21.grid(row=3, column=2)

        self.Button22 = Button(self, activebackground="#d9d9d9", activeforeground="#341a87", background="#e1ccd5",
                               disabledforeground="#ffe5e5", foreground="#341a87", highlightcolor="black",
                               relief=SUNKEN,
                               height=2, width=5, pady="0", padx="0",
                               command=lambda: self.make_move(3, 3, self.Button22, self.Button21, self.Button16,
                                                              self.Button27, self.Button23, self.Button29,
                                                              self.Button28, self.Button17, self.Button15))
        self.Button22.grid(row=3, column=3)

        self.Button23 = Button(self, activebackground="#d9d9d9", activeforeground="#341a87", background="#e1ccd5",
                               disabledforeground="#ffe5e5", foreground="#341a87", highlightcolor="black",
                               relief=SUNKEN,
                               height=2, width=5, pady="0", padx="0",
                               command=lambda: self.make_move(3, 4, self.Button23, self.Button22, self.Button28,
                                                              self.Button24, self.Button17, self.Button30,
                                                              self.Button16, self.Button29, self.Button18))
        self.Button23.grid(row=3, column=4)

        self.Button24 = Button(self, activebackground="#d9d9d9", activeforeground="#341a87", background="#e1ccd5",
                               disabledforeground="#ffe5e5", foreground="#341a87", highlightcolor="black",
                               relief=SUNKEN,
                               height=2, width=5, pady="0", padx="0",
                               command=lambda: self.make_move(3, 5, self.Button24, self.Button23, self.Button29,
                                                              self.Button18, self.Button17, self.Button30,
                                                              self.Button_nineteen, self.Button_twentyfive,
                                                              self.Button_thirtyone))
        self.Button24.grid(row=3, column=5)

        self.Button_twentyfive = Button(self, activebackground="#d9d9d9", activeforeground="#341a87", background="#e1ccd5",
                               disabledforeground="#ffe5e5", foreground="#341a87", highlightcolor="black",
                               relief=SUNKEN,
                               height=2, width=5, pady="0", padx="0",
                               command=lambda: self.make_move(3, 6, self.Button_twentyfive, self.Button24,
                                                              self.Button18, self.Button30,
                                                              self.Button_nineteen, self.Button_thirtyone,
                                                              self.Button_twenty, self.Button_twentysix, self.Button_thirytwo))
        self.Button_twentyfive.grid(row=3, column=6)

        self.Button_twentysix = Button(self, activebackground="#d9d9d9", activeforeground="#341a87", background="#e1ccd5",
                               disabledforeground="#ffe5e5", foreground="#341a87", highlightcolor="black",
                               relief=SUNKEN,
                               height=2, width=5, pady="0", padx="0",
                               command=lambda: self.make_move(3, 7, self.Button_twentysix, self.Button_nineteen, self.Button_twenty,
                                                              self.Button_twentyfive, self.Button_thirtyone, self.Button_thirytwo))
        self.Button_twentysix.grid(row=3, column=7)

        """ROW 4"""

        self.Button25 = Button(self, activebackground="#d9d9d9", activeforeground="#341a87", background="#e1ccd5",
                               disabledforeground="#ffe5e5", foreground="#341a87", highlightcolor="black",
                               relief=SUNKEN,
                               height=2, width=5, pady="0", padx="0",
                               command=lambda: self.make_move(4, 0, self.Button25, self.Button31, self.Button32,
                                                              self.Button19, self.Button26, self.Button20))
        self.Button25.grid(row=4, column=0)

        self.Button26 = Button(self, activebackground="#d9d9d9", activeforeground="#341a87", background="#e1ccd5",
                               disabledforeground="#ffe5e5", foreground="#341a87", highlightcolor="black",
                               relief=SUNKEN,
                               height=2, width=5, pady="0", padx="0",
                               command=lambda: self.make_move(4, 1, self.Button26, self.Button19, self.Button21,
                                                              self.Button25, self.Button32, self.Button20,
                                                              self.Button31, self.Button27, self.Button33))
        self.Button26.grid(row=4, column=1)

        self.Button27 = Button(self, activebackground="#d9d9d9", activeforeground="#341a87", background="#e1ccd5",
                               disabledforeground="#ffe5e5", foreground="#341a87", highlightcolor="black",
                               relief=SUNKEN,
                               height=2, width=5, pady="0", padx="0",
                               command=lambda: self.make_move(4, 2, self.Button27, self.Button20, self.Button26,
                                                              self.Button34, self.Button22, self.Button28,
                                                              self.Button33, self.Button32, self.Button21))
        self.Button27.grid(row=4, column=2)

        self.Button28 = Button(self, activebackground="#d9d9d9", activeforeground="#341a87", background="#e1ccd5",
                               disabledforeground="#ffe5e5", foreground="#341a87", highlightcolor="black",
                               relief=SUNKEN,
                               height=2, width=5, pady="0", padx="0",
                               command=lambda: self.make_move(4, 3, self.Button28, self.Button21, self.Button33,
                                                              self.Button27, self.Button23, self.Button29,
                                                              self.Button22, self.Button35, self.Button34))
        self.Button28.grid(row=4, column=3)

        self.Button29 = Button(self, activebackground="#d9d9d9", activeforeground="#341a87", background="#e1ccd5",
                               disabledforeground="#ffe5e5", foreground="#341a87", highlightcolor="black",
                               relief=SUNKEN,
                               height=2, width=5, pady="0", padx="0",
                               command=lambda: self.make_move(4, 4, self.Button29, self.Button22, self.Button28,
                                                              self.Button24, self.Button36, self.Button30,
                                                              self.Button35, self.Button23, self.Button34))
        self.Button29.grid(row=4, column=4)

        self.Button30 = Button(self, activebackground="#d9d9d9", activeforeground="#341a87", background="#e1ccd5",
                               disabledforeground="#ffe5e5", foreground="#341a87", highlightcolor="black",
                               relief=SUNKEN,
                               height=2, width=5, pady="0", padx="0",
                               command=lambda: self.make_move(4, 5, self.Button30, self.Button23, self.Button29,
                                                              self.Button35, self.Button36, self.Button24,
                                                              self.Button_twentyfive, self.Button_thirtyone,
                                                              self.Button_thirtyseven))
        self.Button30.grid(row=4, column=5)

        self.Button_thirtyone = Button(self, activebackground="#d9d9d9", activeforeground="#341a87", background="#e1ccd5",
                               disabledforeground="#ffe5e5", foreground="#341a87", highlightcolor="black",
                               relief=SUNKEN,
                               height=2, width=5, pady="0", padx="0",
                               command=lambda: self.make_move(4, 6, self.Button_thirtyone, self.Button_twentyfive, self.Button_twentysix,
                                                              self.Button30, self.Button36, self.Button24,
                                                              self.Button_thirtyseven, self.Button_thirytwo, self.Button_thirtyeight))
        self.Button_thirtyone.grid(row=4, column=6)

        self.Button_thirytwo = Button(self, activebackground="#d9d9d9", activeforeground="#341a87", background="#e1ccd5",
                               disabledforeground="#ffe5e5", foreground="#341a87", highlightcolor="black",
                               relief=SUNKEN,
                               height=2, width=5, pady="0", padx="0",
                               command=lambda: self.make_move(4, 7, self.Button_thirytwo, self.Button_twentysix, self.Button_twentyfive,
                                                              self.Button_thirtyone, self.Button_thirtyseven, self.Button_thirtyeight))
        self.Button_thirytwo.grid(row=4, column=7)

        """ROW 5"""

        self.Button31 = Button(self, activebackground="#d9d9d9", activeforeground="#341a87", background="#e1ccd5",
                               disabledforeground="#ffe5e5", foreground="#341a87", highlightcolor="black",
                               relief=SUNKEN,
                               height=2, width=5, pady="0", padx="0",
                               command=lambda: self.make_move(5, 0, self.Button31, self.Button25, self.Button32,
                                                              self.Button26, self.Button39, self.Button40))
        self.Button31.grid(row=5, column=0)

        self.Button32 = Button(self, activebackground="#d9d9d9", activeforeground="#341a87", background="#e1ccd5",
                               disabledforeground="#ffe5e5", foreground="#341a87", highlightcolor="black",
                               relief=SUNKEN,
                               height=2, width=5, pady="0", padx="0",
                               command=lambda: self.make_move(5, 1, self.Button32, self.Button39, self.Button40,
                                                              self.Button25, self.Button26, self.Button41,
                                                              self.Button31, self.Button27, self.Button33))
        self.Button32.grid(row=5, column=1)

        self.Button33 = Button(self, activebackground="#d9d9d9", activeforeground="#341a87", background="#e1ccd5",
                               disabledforeground="#ffe5e5", foreground="#341a87", highlightcolor="black",
                               relief=SUNKEN,
                               height=2, width=5, pady="0", padx="0",
                               command=lambda: self.make_move(5, 2, self.Button33,  self.Button26, self.Button40,
                                                              self.Button34,  self.Button28, self.Button41,
                                                              self.Button27, self.Button32, self.Button42))
        self.Button33.grid(row=5, column=2)

        self.Button34 = Button(self, activebackground="#d9d9d9", activeforeground="#341a87", background="#e1ccd5",
                               disabledforeground="#ffe5e5", foreground="#341a87", highlightcolor="black",
                               relief=SUNKEN,
                               height=2, width=5, pady="0", padx="0",
                               command=lambda: self.make_move(5, 3, self.Button34, self.Button33,self.Button41,
                                                              self.Button27, self.Button29, self.Button42,
                                                               self.Button35, self.Button28, self.Button43))
        self.Button34.grid(row=5, column=3)

        self.Button35 = Button(self, activebackground="#d9d9d9", activeforeground="#341a87", background="#e1ccd5",
                               disabledforeground="#ffe5e5", foreground="#341a87", highlightcolor="black",
                               relief=SUNKEN,
                               height=2, width=5, pady="0", padx="0",
                               command=lambda: self.make_move(5, 4, self.Button35, self.Button28, self.Button42,
                                                                self.Button36, self.Button30, self.Button43,
                                                              self.Button29, self.Button34, self.Button44))
        self.Button35.grid(row=5, column=4)

        self.Button36 = Button(self, activebackground="#d9d9d9", activeforeground="#341a87", background="#e1ccd5",
                               disabledforeground="#ffe5e5", foreground="#341a87", highlightcolor="black",
                               relief=SUNKEN,
                               height=2, width=5, pady="0", padx="0",
                               command=lambda: self.make_move(5, 5, self.Button36, self.Button29, self.Button43,
                                                              self.Button35, self.Button30, self.Button44, self.Button45,
                                                              self.Button_thirtyone, self.Button_thirtyseven))
        self.Button36.grid(row=5, column=5)

        self.Button_thirtyseven = Button(self, activebackground="#d9d9d9", activeforeground="#341a87", background="#e1ccd5",
                               disabledforeground="#ffe5e5", foreground="#341a87", highlightcolor="black",
                               relief=SUNKEN,
                               height=2, width=5, pady="0", padx="0",
                               command=lambda: self.make_move(5, 6, self.Button_thirtyseven, self.Button44,
                                                              self.Button36, self.Button30, self.Button45,
                                                              self.Button_thirtyone, self.Button_thirytwo,
                                                              self.Button_thirtyeight, self.Button46))
        self.Button_thirtyseven.grid(row=5, column=6)

        self.Button_thirtyeight = Button(self, activebackground="#d9d9d9", activeforeground="#341a87", background="#e1ccd5",
                               disabledforeground="#ffe5e5", foreground="#341a87", highlightcolor="black",
                               relief=SUNKEN,
                               height=2, width=5, pady="0", padx="0",
                               command=lambda: self.make_move(5, 7, self.Button_thirtyeight, self.Button45,
                                                              self.Button_thirytwo, self.Button46,
                                                              self.Button_thirtyone, self.Button_thirtyseven))
        self.Button_thirtyeight.grid(row=5, column=7)

        """ROW 6"""

        self.Button39 = Button(self, activebackground="#d9d9d9", activeforeground="#341a87", background="#e1ccd5",
                               disabledforeground="#ffe5e5", foreground="#341a87", highlightcolor="black",
                               relief=SUNKEN,
                               height=2, width=5, pady="0", padx="0",
                               command=lambda: self.make_move(6, 0, self.Button39, self.Button31, self.Button32,
                                                              self.Button40))
        self.Button39.grid(row=6, column=0)

        self.Button40 = Button(self, activebackground="#d9d9d9", activeforeground="#341a87", background="#e1ccd5",
                               disabledforeground="#ffe5e5", foreground="#341a87", highlightcolor="black",
                               relief=SUNKEN,
                               height=2, width=5, pady="0", padx="0",
                               command=lambda: self.make_move(6, 1, self.Button40,
                                                              self.Button41, self.Button39,
                                                              self.Button31, self.Button32, self.Button33))
        self.Button40.grid(row=6, column=1)

        self.Button41 = Button(self, activebackground="#d9d9d9", activeforeground="#341a87", background="#e1ccd5",
                               disabledforeground="#ffe5e5", foreground="#341a87", highlightcolor="black",
                               relief=SUNKEN,
                               height=2, width=5, pady="0", padx="0",
                               command=lambda: self.make_move(6, 2, self.Button41, self.Button40,
                                                              self.Button42, self.Button33,
                                                              self.Button34, self.Button32))
        self.Button41.grid(row=6, column=2)

        self.Button42 = Button(self, activebackground="#d9d9d9", activeforeground="#341a87", background="#e1ccd5",
                               disabledforeground="#ffe5e5", foreground="#341a87", highlightcolor="black",
                               relief=SUNKEN,
                               height=2, width=5, pady="0", padx="0",
                               command=lambda: self.make_move(6, 3, self.Button42, self.Button33,
                                                              self.Button34,
                                                              self.Button35, self.Button41, self.Button43))
        self.Button42.grid(row=6, column=3)

        self.Button43 = Button(self, activebackground="#d9d9d9", activeforeground="#341a87", background="#e1ccd5",
                               disabledforeground="#ffe5e5", foreground="#341a87", highlightcolor="black",
                               relief=SUNKEN,
                               height=2, width=5, pady="0", padx="0",
                               command=lambda: self.make_move(6, 4, self.Button43, self.Button35,
                                                              self.Button36, self.Button42,
                                                              self.Button44, self.Button34))
        self.Button43.grid(row=6, column=4)

        self.Button44 = Button(self, activebackground="#d9d9d9", activeforeground="#341a87", background="#e1ccd5",
                               disabledforeground="#ffe5e5", foreground="#341a87", highlightcolor="black",
                               relief=SUNKEN,
                               height=2, width=5, pady="0", padx="0",
                               command=lambda: self.make_move(6, 5, self.Button44, self.Button36, self.Button43,
                                                              self.Button35, self.Button_thirtyseven, self.Button45))
        self.Button44.grid(row=6, column=5)

        self.Button45 = Button(self, activebackground="#d9d9d9", activeforeground="#341a87",
                                         background="#e1ccd5",
                                         disabledforeground="#ffe5e5", foreground="#341a87", highlightcolor="black",
                                         relief=SUNKEN,
                                         height=2, width=5, pady="0", padx="0",
                                         command=lambda: self.make_move(6, 6, self.Button45, self.Button_thirtyseven,
                                                                        self.Button36, self.Button_thirtyeight,
                                                                        self.Button44, self.Button46))
        self.Button45.grid(row=6, column=6)

        self.Button46 = Button(self, activebackground="#d9d9d9", activeforeground="#341a87",
                                         background="#e1ccd5",
                                         disabledforeground="#ffe5e5", foreground="#341a87", highlightcolor="black",
                                         relief=SUNKEN,
                                         height=2, width=5, pady="0", padx="0",
                                         command=lambda: self.make_move(6, 7, self.Button46, self.Button_thirtyeight,
                                                                        self.Button_thirtyseven, self.Button45))
        self.Button46.grid(row=6, column=7)


        self.button_array = {}
        iterate = 0
        for but in (self.Button1, self.Button2, self.Button3, self.Button4, self.Button5, self.Button6,
                    self.Button_seven, self.Button_eight, self.Button7,
                    self.Button8, self.Button9, self.Button10, self.Button11, self.Button12,
                    self.Button_thirteen, self.Button_fourteen, self.Button13, self.Button14,
                    self.Button15, self.Button16, self.Button17, self.Button18,
                    self.Button_nineteen, self.Button_twenty, self.Button19, self.Button20,
                    self.Button21, self.Button22, self.Button23, self.Button24,
                    self.Button_twentyfive, self.Button_twentysix, self.Button25, self.Button26,
                    self.Button27, self.Button28, self.Button29, self.Button30,
                    self.Button_thirtyone, self.Button_thirytwo, self.Button31, self.Button32,
                    self.Button33, self.Button34, self.Button35, self.Button36,
                    self.Button_thirtyseven, self.Button_thirtyeight, self.Button39, self.Button40, self.Button41,
                    self.Button42, self.Button43, self.Button44, self.Button45, self.Button46):
            self.button_array[iterate] = but
            iterate += 1

        fill_in = Button(self, borderwidth="0")
        fill_in.grid(row=0, column=8)
        lbl_info = Label(self, font=('terminal', 15, 'bold'), text="7x8 Board", anchor='w')
        lbl_info.grid(row=0, column=9)
        self.ButtonQuit = Button(self, background="#DA2C43", text="Quit", height=2, width=5,
                                 command=lambda: self.quit())
        self.ButtonQuit.grid(row=2, column=9)
        self.ButtonReset = Button(self, background="light green", text="Reset", height=2, width=5,
                                  command=lambda: self.reset_game())
        self.ButtonReset.grid(row=1, column=9)

    def create_board(self):
        self.__ai.set_row(7)
        self.__ai.set_column(8)
        self.__ai.create_board()

    def quit(self):
        self.destroy = 1
        self.ButtonReset.invoke()
        self.__ctr.quit_frame()

    def make_move(self, x, y, *buttons):
        try:
            if self.in_turn == 1:
                self.__ai.make_move_player(x, y)
                for button in buttons:
                    button.configure(bg="#B2BEB5")
                buttons[0].configure(text="0", fg="#315e1d", bg="#e7d6d6")
                if self.__ai.game_over() is False:
                    messagebox.showinfo("Congratulations!", "You are a winner!...This time :P")
                    return
                self.in_turn = 2
                point = self.__ai.make_move_ai(self.first, x, y)
                index = point.get_x() * 8 + point.get_y()
                self.button_array[index].invoke()
            if self.in_turn == 2:
                for button in buttons:
                    button.configure(bg="#B2BEB5")
                buttons[0].configure(text="X", fg="#770505", bg="#e7d6d6")
                self.in_turn = 1
                if self.__ai.game_over() is False:
                    messagebox.showinfo("Better luck next time...", "HAHA I WON!")
                    return

        except Exception as error:
            messagebox.showinfo("Error", "Invalid move: " + str(error))

    def first_ai(self):
        self.first = 1
        self.in_turn = 2
        point = self.__ai.make_move_ai(self.first, 0, 0)
        index = point.get_x() * 8 + point.get_y()
        self.button_array[index].invoke()

    def reset_game(self):
        if self.destroy== 1:
            # If the user wants to quit the frame, we only destroy the board and reset the buttons
            self.__ai.destroy_board()
            self.destroy = 0
            self.first = 0
            for x in range(0, 56):
                self.button_array[x].configure(text='', bg="white")
        else:
            # Otherwise we destroy, recreate the board with the specific dimension and reset the buttons
            self.__ai.destroy_board()
            self.__ai.set_row(7)
            self.__ai.set_column(8)
            self.__ai.create_board()
            self.in_turn = 1
            for x in range(0, 56):
                self.button_array[x].configure(text='', bg="white")
            if self.first == 1:
                self.first_ai()
