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
        """
        This method initializes the window and creates all global variables
        :param parent: the parent of the frame
        :param title: the title for the window
        """
        Frame.__init__(self, parent)
        self.title, self.style, self.parent = title, Style(), parent
        self.width, self.height = self.parent.winfo_screenwidth(), self.parent.winfo_screenheight()

        self.parent.title(self.title)
        self.parent.geometry("%dx%d" % (self.width, self.height))

    def pack_window(self):
        self.pack(fill=BOTH, expand=1)

    def add_tabs(self, tabs=3):
        note_book = Notebook(self.parent)
        for i in range(tabs):
            self.add_tab(note_book, "Testing")
        note_book.pack()

    def setup_grid(self, rows=5, columns=5):
        content = Frame(self.parent)
        content.grid(column=0, row=0, columnspan=columns, rowspan=rows)

        canvas_width = (self.width * 0.9) / columns
        canvas_height = (self.height * 0.9) / rows
        canvas_list = []
        for i in range(columns):
            for j in range(rows):
                label_text = '| ' + str(i) + ', ' + str(j) + ' |'
                canvas = Canvas(content, width=canvas_width, height=canvas_height)

                canvas.pack(side="top", fill="both", expand=True)
                canvas_id = canvas.create_text(10, 10, anchor="nw")

                canvas.itemconfig(canvas_id, text=label_text)
                canvas.insert(canvas_id, 12, "")

                canvas_list.append(canvas)
                canvas_list[(i * rows) + j].grid(column=i, row=j)

    @staticmethod
    def add_tab(note_book, text):
        tab = Frame()

        note_book.add(tab, text=text)


def main():
    root = Tk()
    root.maxsize()
    comp_finance_window = Window(root, "Computational Finance Package")
    #comp_finance_window.add_tabs()
    comp_finance_window.setup_grid(10, 15)
    comp_finance_window.pack_window()

    root.mainloop()

if __name__ == '__main__':
    main()