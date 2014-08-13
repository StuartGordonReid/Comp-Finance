__author__ = 'Stuart Gordon Reid'
__email__ = 'stuartgordonreid@gmail.com'
__website__ = 'http://www.stuartreid.co.za'

"""
This file contains the primary window for interfacing with the Computational Finance package. It will act as a container
for various frames related to computational finance especially w.r.t portfolio construction and optimization
"""

from Tkinter import *
from ttk import *
from Overview import Overview


class Window(Frame):
    """
    This class contains the primary window (frame) within which additional frames will be added
    """

    width, height = 0, 0

    def __init__(self, parent, title):
        Frame.__init__(self, parent)
        self.title = title
        self.style = Style()
        self.parent = parent
        self.parent.title(self.title)

    def init_window(self):
        self.width = self.parent.winfo_screenwidth()
        self.height = self.parent.winfo_screenheight()
        self.parent.geometry("%dx%d" % (self.width, self.height))
        self.pack(fill=BOTH, expand=1)

    def add_tabs(self, tabs=3):
        note_book = Notebook(self.parent)
        for i in range(tabs):
            self.add_tab(note_book, "Testing")
        note_book.pack()

    @staticmethod
    def add_tab(note_book, text):
        tab = Overview()
        note_book.add(tab, text=text)


def main():
    root = Tk()
    comp_finance_window = Window(root, "Computational Finance Package")
    comp_finance_window.add_tabs()
    comp_finance_window.init_window()

    root.mainloop()

if __name__ == '__main__':
    main()