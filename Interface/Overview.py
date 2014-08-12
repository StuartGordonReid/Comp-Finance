__author__ = 'Stuart Gordon Reid'
__email__ = 'stuartgordonreid@gmail.com'
__website__ = 'http://www.stuartreid.co.za'

"""
File description
"""

from Tkinter import *
from ttk import *


class Overview(Frame):
    """
    This class contains the code to create an 'Overview' Tab for a portfolio
    """
    def __init__(self, **kw):
        Frame.__init__(self, **kw)
        table = SimpleTable(self, 10, 2)
        table.pack(side="top", fill="x")
        table.set(0, 0, "Hello, world")


class SimpleTable(Frame):
    """
    This class contains code to create a simple table
    """
    def __init__(self, parent, rows=10, columns=2):
        # use black background so it "peeks through" to
        # form grid lines
        Frame.__init__(self, parent)
        self._widgets = []
        for row in range(rows):
            current_row = []
            for column in range(columns):
                label = Label(self, text="%s/%s" % (row, column), borderwidth=0, width=10)
                label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                current_row.append(label)
            self._widgets.append(current_row)

        for column in range(columns):
            self.grid_columnconfigure(column, weight=1)

    def set(self, row, column, value):
        widget = self._widgets[row][column]
        widget.configure(text=value)