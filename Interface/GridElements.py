__author__ = 'Stuart Gordon Reid'
__email__ = 'stuartgordonreid@gmail.com'
__website__ = 'http://www.stuartreid.co.za'

"""
This file contains a collection of Grid Elements which can be used by the primary window object. These files include,

GridElement :- Abstract Base Class & Canvas
TextGridElement :- Grid Element containing text
ImageGridElement :- Grid Element containing an image
"""

from Tkinter import *
from ttk import *
import abc


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