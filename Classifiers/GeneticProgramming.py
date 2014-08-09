__author__ = 'Stuart Gordon Reid'
__email__ = 'stuartgordonreid@gmail.com'
__website__ = 'http://www.stuartreid.co.za'

"""
File description
"""

from Optimizers.GeneticAlgorithm import GeneticAlgorithm
from Optimizers.Solution import Solution

__author__ = 'stuartreid'


class GeneticProgramming(GeneticAlgorithm):
    """
    This class contains a generic Genetic Programming (GP) algorithm implementation. This algorithm evolves a set of
    Individuals which represent tree-based solutions to a particular problem (Function object)
    """

    def __init__(self, problem, parameters=None):
        super(GeneticProgramming, self).__init__(problem, parameters)

    def selection(self):
        pass

    def crossover(self):
        pass

    def mutation(self):
        pass

