__author__ = 'Stuart Gordon Reid'
__email__ = 'stuartgordonreid@gmail.com'
__website__ = 'http://www.stuartreid.co.za'

"""
This file contains the primary window for interfacing with the Computational Finance package. It will act as a container
for various frames related to computational finance especially w.r.t portfolio construction and optimization
"""

from Tkinter import *
from ttk import *
import abc


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

        # Initialize global variables
        Frame.__init__(self, parent)
        self.title, self.style, self.parent = title, Style(), parent
        self.width, self.height = self.parent.winfo_screenwidth(), self.parent.winfo_screenheight()

        # Configure properties of global variables
        self.parent.title(self.title)
        self.content_grid = Frame(self.parent)
        self.parent.geometry("%dx%d" % (self.width, self.height))

    def pack_window(self):
        """
        This method just 'packs' the window with the different components
        """
        self.pack(fill=BOTH, expand=1)

    def setup_grid(self, padding=1.0, rows=5, columns=5, grid_elements=None):
        """
        This method initializes a grid within the root window
        :param grid_elements: the particular layout for the canvases
        :param rows: the number of rows to create
        :param columns: the number of columns to create
        """
        self.content_grid.grid(column=0, row=0, columnspan=columns, rowspan=rows)
        self.fill_grid(padding, rows, columns, grid_elements)

    def fill_grid(self, padding=1.0, rows=5, columns=5, grid_elements=None):
        """
        This method creates elements (canvases) inside of the grid and links to them
        :param grid_elements: the particular layout for the canvases
        :param rows: the number of rows to create
        :param columns: the number of columns to create
        """
        one_width = (self.width * padding) / columns
        one_height = (self.height * padding) / rows
        for element in grid_elements:
            assert isinstance(element, GridElement)
            canvas_width = one_width * element.x_length
            canvas_height = one_height * element.y_length
            element.canvas = Canvas(self.content_grid, width=canvas_width, height=canvas_height)
            element.canvas.configure(bg=element.colour)
            element.canvas.grid(column=element.x, row=element.y, columns=element.x_length, rows=element.y_length)

    def add_tabs(self, tabs=3):
        """
        This is a method for adding tabs to the window
        :param tabs: the number of tabs to add to the window
        """
        note_book = Notebook(self.parent)
        for i in range(tabs):
            tab = Frame()
            note_book.add(tab, text="Hello World!")
        note_book.pack()


class GridElement():
    """
    This class contains data for grid elements
    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def __init__(self, x, y, x_length, y_length, colour="black"):
        self.x, self.y, self.colour = x, y, colour
        self.x_length, self.y_length = x_length, y_length
        self.canvas = None

    @abc.abstractmethod
    def add_elements(self):
        pass


class FormGridElement(GridElement):
    """
    This class contains data for grid elements
    """
    def __init__(self, x, y, x_length, y_length, colour="black"):
        GridElement.__init__(self, x, y, x_length, y_length, colour)

    def add_elements(self):
        assert isinstance(self.canvas, Canvas)
        button = Button(self.canvas, text="Quit")
        label = Label(self.canvas, text="This is a label")
        window_one = self.canvas.create_window(10, 10, anchor=NW, window=label)
        window_two = self.canvas.create_window(100, 10, anchor=NW, window=button)


def main():
    root = Tk()
    top_level = root.winfo_toplevel()
    top_level.wm_state('zoomed')
    comp_finance_window = Window(root, "Computational Finance Package")

    grid_elements = [FormGridElement(0, 0, 10, 1, 'blue'),
                     FormGridElement(0, 1, 10, 8, 'black'),
                     FormGridElement(0, 9, 10, 1, 'blue')]
    comp_finance_window.setup_grid(0.95, 10, 10, grid_elements)

    for element in grid_elements:
        element.add_elements()

    comp_finance_window.pack_window()
    root.mainloop()

if __name__ == '__main__':
    main()