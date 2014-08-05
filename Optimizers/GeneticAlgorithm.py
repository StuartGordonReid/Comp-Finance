from Optimizers.Optimizer import Optimizer

__author__ = 'stuartreid'


class GeneticAlgorithm(Optimizer):
    """
    This class contains a generic implementation of the Genetic Algorithm. It uses Selection, Mutation, and Crossover
    objects to evolve a population of candidate solutions to a particular optimization problem.
    """

    def __init__(self, problem, parameters):
        super(GeneticAlgorithm, self).__init__(problem, parameters)

    def optimize(self, iterations=1000, stopping=True):
        pass

