__author__ = 'Stuart Gordon Reid'
__email__ = 'stuartgordonreid@gmail.com'
__website__ = 'http://www.stuartreid.co.za'

"""
File description
"""

import abc


class Sorter():
    """
    This abstract base class contains code for a generic sorter. A sorter is an algorithm which receives some form of
    data and sorts it in a particular order
    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def __init__(self, data, ordering="ascending"):
        """
        Initialization method for a genetic sorter
        :param data: the list of data to be sorted by the algorithm
        :param ordering: the order in which to sort that data
        """
        self.data = data
        self.ordering = ordering

    @abc.abstractmethod
    def sort(self):
        """
        Abstract sort method to be overloaded by sorting algorithms
        :return: returns the sorted data (list)
        """
        return self.data

