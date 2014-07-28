__author__ = 'Stuart Gordon Reid'
__email__ = 'stuartgordonreid@gmail.com'
__website__ = 'http://www.stuartreid.co.za'

"""
File description
"""

import abc


class Solution(object):
    __metaclass__ = abc.ABCMeta
    solution = []

    @abc.abstractmethod
    def __init__(self, solution):
        """
        Abstract initialization method for a solution to some optimization function
        :param solution: a numpy array (much faster than lists)
        """
        self.solution = solution
        return

    @property
    def __len__(self):
        """
        Overload of the len operator for the Solution class
        :rtype : Sized?
        """
        return len(self.solution)

    def update(self, solution):
        """
        This method is used for updating a solution
        """
        self.solution = solution

    def get(self):
        """
        This method is used to retrieve the numpy array for direct manipulation
        """
        return self.solution
