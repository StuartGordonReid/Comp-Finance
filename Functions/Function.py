__author__ = 'Stuart Gordon Reid'
__email__ = 'stuartgordonreid@gmail.com'
__website__ = 'http://www.stuartreid.co.za'

"""
A generic class for optimization test functions. The information used here is taken from the GO Test Problems website
which can be found here: http://www-optima.amp.i.kyoto-u.ac.jp/member/student/hedar/Hedar_files/TestGO_files/Page364.htm
"""

import abc
from Optimizers.Optimizer import Solution


class Function(object):
    __metaclass__ = abc.ABCMeta
    dimension = 0

    @abc.abstractmethod
    def __init__(self, dimension):
        """
        This method should be overloaded and used to initialize the problem
        :param dimension: the dimension on the problem
        """
        self.dimension = dimension
        return

    @abc.abstractmethod
    def evaluate(self, candidate):
        """
        This method should be overloaded and used to evaluate a candidate solution to the problem
        :param candidate: the candidate solution to the problem
        """
        assert isinstance(candidate, Solution)
        return
