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

    __children__ = []
    __data__ = None
    __size__ = 0
    __count__ = 0

    def __init__(self, data=None):
        self.__children__ = []
        self.__data__ = data
        self.__size__ = 0
        pass

    # Generic getter and setter methods used to index the children array

    def get(self, index):
        """
        Generic get method which handles retrieval of data from the children array
        :param index: index of the item in children to be returned
        :return: returns the AbstractNode at the index specific, could be None
        """
        if index < self.__size__:
            return self.__children__[index]
        else:
            return None

    def set(self, index, value):
        """
        Generic set method for inputting data into the children array
        :param index: index of the item in children to be updated
        :param value: An Abstract Node to overwrite the value of children[index]
        """
        if (index + 1) > self.__size__:
            for i in range((index + 1) - self.__size__):
                self.__children__.append(None)
                self.__size__ += 1
            self.__children__[index] = value
        else:
            self.__children__[index] = value

    # Definition of the get_next() and set_next() methods for binary structures

    def get_next(self):
        return self.get(0)

    def set_next(self, new_abstract_node):
        self.set(0, new_abstract_node)

    def get_prev(self):
        return self.get(1)

    def set_prev(self, new_abstract_node):
        self.set(1, new_abstract_node)

    # Definition of the get_left(), get_right() and set_left(), set_right methods for binary structures

    def get_left(self):
        return self.get(2)

    def set_left(self, new_abstract_node):
        self.set(2, new_abstract_node)

    def get_right(self):
        return self.get(3)

    def set_right(self, new_abstract_node):
        self.set(3, new_abstract_node)

    # For setting this object's data

    def get_data(self):
        return self.__data__

    def set_data(self, data):
        self.__data__ = data

    def increment(self):
        self.__count__ += 1


if __name__ == "__main__":
    # Testing method
    my_node = AbstractNode()
    print(len(my_node.__children__))

    my_node.set_next(AbstractNode())
    print(len(my_node.__children__))

    my_node.set_next(AbstractNode())
    print(len(my_node.__children__))

    my_node.set_prev(AbstractNode())
    print(len(my_node.__children__))

    my_node.set_left(AbstractNode())
    print(len(my_node.__children__))

    my_node.set_right(AbstractNode())
    print(len(my_node.__children__))

    my_node.set_right(AbstractNode())
    print(len(my_node.__children__))