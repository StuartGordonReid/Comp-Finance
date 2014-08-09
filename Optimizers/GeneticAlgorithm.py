__author__ = 'Stuart Gordon Reid'
__email__ = 'stuartgordonreid@gmail.com'
__website__ = 'http://www.stuartreid.co.za'

"""
File description
"""

import random
from Optimizers.Optimizer import Optimizer
from Optimizers.Solution import Solution


class GeneticAlgorithm(Optimizer):
    """
    This class contains a generic implementation of the Genetic Algorithm. It uses Selection, Mutation, and Crossover
    objects to evolve a population of candidate solutions to a particular optimization problem.
    """

    def __init__(self, problem, parameters=None):
        """
        Initialization method for the Genetic Algorithm
        :param problem:
        :param parameters[0]: Crossover rate (% of the population which is used in crossover)
        :param parameters[1]: Crossover strategy e.g. sexual, asexual
        :param parameters[2]: Mutation rate (% of the population which is mutated)
        :param parameters[3]: Mutator strategy e.g. Brownian Individuals
        :param parameters[4]: Selection rate (% of the population to be culled)
        :param parameters[5]: Selection strategy e.g. Rank Selection vs. Random Selection
        :param parameters[6]: Population size # individuals.
        """
        if parameters is None:
            parameters = [0.5, "sexual", 0.05, "brownian", 0.5, "rank", 50]
        super(GeneticAlgorithm, self).__init__(problem, parameters)
        self.population = []
        for i in range(parameters[6]):
            random_solution = random.sample(xrange(problem.lower_bound, problem.upper_bound), problem.dimension)
            self.population.append(Individual(random_solution, problem))

    def optimize(self, iterations=1000, stopping=True):
        pass

    def select(self):
        pass

    def crossover(self):
        pass

    def mutate(self):
        pass


class Individual(Solution):
    """
    This class contains the code required to create an individual
    """

    def __init__(self, solution, problem):
        """
        Initialization method for Individuals
        :param solution:
        :param problem:
        """
        super(Individual, self).__init__(solution, problem)

