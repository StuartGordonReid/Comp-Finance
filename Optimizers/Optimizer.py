__author__ = 'Stuart Gordon Reid'
__email__ = 'stuartgordonreid@gmail.com'
__website__ = 'http://www.stuartreid.co.za'

"""
File description
"""

import abc
import numpy as np
import Functions


class Optimizer(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def __init__(self, problem, parameters):
        """
        This method initialized the Optimizer with an objective function and a set of parameters
        :param problem: this is the problem being optimized
        :param parameters: set of algorithm control parameters
        """
        self.problem = problem
        self.parameters = parameters
        return

    @abc.abstractmethod
    def optimize(self, iterations=1000, stopping=True):
        """
        This is the generic optimization method to be overloaded by each optimizer
        :param stopping: whether or not the algorithm should use early stopping
        :param iterations: the number of iterations to optimize for, default is 1000
        """
        return

    def fitness(self, candidate):
        """
        This is the generic optimization method to be overloaded by each optimizer
        :param candidate:
        """
        assert isinstance(self.problem, Functions.Function)
        assert isinstance(candidate, Solution)
        return self.problem.evaluate(candidate)



