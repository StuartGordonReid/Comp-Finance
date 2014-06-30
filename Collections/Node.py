__author__ = 'Stuart Gordon Reid'
__email__ = 'stuartgordonreid@gmail.com'
__website__ = 'http://www.stuartreid.co.za'

"""
This file contains the implementation of the Abstract Node class
"""


class AbstractNode:
    """
    This abstract node class is used as the basis of the data-structures which make up the Python Collection package.
    It is implemented with a generic get(x) function which returns the child of Abstract Node at x. This is overloaded
    by methods next(), left(), and right() when implementing linked-lists, queues, stacks, and trees.
    """

    children = []
    data = None

    def __init__(self, data=None):
        self.children = [None, None, None]
        self.data = data
        pass

    # Generic getter and setter methods used to index the children array

    def get(self, index):
        """
        Generic get method which handles retrieval of data from the children array
        :param index: index of the item in children to be returned
        :return: returns the AbstractNode at the index specific, could be None
        """
        return self.children[index]

    def set(self, index, value):
        """
        Generic set method for inputting data into the children array
        :param index: index of the item in children to be updated
        :param value: An Abstract Node to overwrite the value of children[index]
        """
        self.children[index] = value

    # Definition of the get_next() and set_next() methods for binary structures

    def get_next(self):
        return self.get(0)

    def set_next(self, data):
        self.set(0, data)

    # Definition of the get_left(), get_right() and set_left(), set_right methods for binary structures

    def get_left(self):
        return self.get(1)

    def set_left(self, data):
        self.set(1, data)

    def get_right(self):
        return self.get(2)

    def set_right(self, data):
        self.set(2, data)
