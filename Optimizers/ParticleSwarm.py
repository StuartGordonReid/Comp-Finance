__author__ = 'Stuart Gordon Reid'
__email__ = 'stuartgordonreid@gmail.com'
__website__ = 'http://www.stuartreid.co.za'

"""
File description
"""

from Optimizers.Optimizer import Optimizer
from Optimizers.Optimizer import Solution
import numpy as np
import random


class ParticleSwarm(Optimizer):
    """
    This class contains an implementation of a standard no-frills Particle Swarm Optimizer
    """

    def __init__(self, problem, parameters=None):
        """
        Initialization method for the Particle Swarm Optimizer
        :param problem: the problem being optimized
        :param parameters: 0 = Inertia, 1 = Cognitive Component (C1), 2 = Social Component (C2)
        """
        #Don't ask me why, http://effbot.org/zone/default-values.htm
        if parameters is None:
            parameters = [0.729844, 1.496180, 1.496180]
        super(ParticleSwarm, self).__init__(problem, parameters)

    def optimize(self, iterations=1000, stopping=True):
        pass


class Particle(Solution):
    def __init__(self, solution, best_solution, velocity):
        """
        Overloaded solution object for the Particle Swarm Optimizer
        :param solution:
        :param velocity:
        :param best_solution:
        """
        assert isinstance(solution, np.array)
        assert isinstance(velocity, np.array)
        assert isinstance(best_solution, np.array)

        self.velocity = velocity
        self.best_solution = best_solution
        #Updates the solution numpy array in super
        super(Particle, self).__init__(solution)

    def update_velocities(self):
        self.velocity = np.array(0)
        return

    def update_solution(self):
        self.solution = np.array(0)
        return