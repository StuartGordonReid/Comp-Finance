__author__ = 'Stuart Gordon Reid'
__email__ = 'stuartgordonreid@gmail.com'
__website__ = 'http://www.stuartreid.co.za'

"""
File description
"""

from Optimizers.Optimizer import Optimizer


class SimulatedAnnealing(Optimizer):

    def __init__(self, problem, parameters):
        """

            :param problem:
            :param parameters:
            """
        super(SimulatedAnnealing, self).__init__(problem, parameters)

    def optimize(self, iterations=1000, stopping=True):
        """

        :param iterations:
        :param stopping:
        """
        pass