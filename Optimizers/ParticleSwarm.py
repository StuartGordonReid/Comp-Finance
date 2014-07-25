__author__ = 'Stuart Gordon Reid'
__email__ = 'stuartgordonreid@gmail.com'
__website__ = 'http://www.stuartreid.co.za'

"""
File description
"""

from Functions.Function import Function
from Optimizers.Optimizer import Optimizer
from Optimizers.Optimizer import Solution
import random


class ParticleSwarm(Optimizer):
    """
    This class contains an implementation of a standard no-frills Particle Swarm Optimizer
    """

    def __init__(self, problem, parameters=None):
        """
        Initialization method for the Particle Swarm Optimizer
        :param problem: the problem being optimized
        :param parameters: 0 = Inertia, 1 = Cognitive Component (C1), 2 = Social Component (C2), 3 = Swarm Size
        """
        assert isinstance(problem, Function)
        #Don't ask me why, http://effbot.org/zone/default-values.htm
        if parameters is None:
            parameters = [0.729844, 1.496180, 1.496180, 50]
        super(ParticleSwarm, self).__init__(problem, parameters)

        #Create swarm
        self.swarm = []
        #Initialize each particle
        for i in range(parameters[3]):
            velocities = [0] * problem.dimension
            random_solution = random.sample(xrange(problem.lower_bound, problem.upper_bound), problem.dimension)
            self.swarm[i] = Particle(random_solution, random_solution, velocities)

    def optimize(self, iterations=1000, stopping=True):
        pass


class Particle(Solution):
    """
    This class is an implementation of the Particle used in a PSO. Particle updates consist of two steps, calculating
    the new velocities and updating them, then calculating the new position by adding the velocities to the position
    """

    def __init__(self, solution, best_solution, velocity):
        """
        Overloaded solution object for the Particle Swarm Optimizer
        :param solution:
        :param velocity:
        :param best_solution:
        """
        self.velocity = velocity
        self.best_solution = best_solution
        #Updates the solution numpy array in super
        super(Particle, self).__init__(solution)

    def update_velocity(self, global_best_solution, parameters=None):
        """
        This method updates the Particles velocity w.r.t the global best and control parameters
        """
        if parameters is None:
            parameters = [0.729844, 1.496180, 1.496180]

        #TODO: Find Pythonic way to do this
        for i in range(len(self.solution)):
            cognitive = parameters[1] * random.random() * (self.best_solution[i] - self.solution[i])
            social = parameters[2] * random.random() * (global_best_solution[i] - self.solution[i])
            self.velocity[i] = parameters[0] * self.velocity[i] + social + cognitive
        return

    def update_solution(self):
        """
        This method updates the Particles position in space
        """
        #TODO: Find Pythonic way to do this
        for i in range(len(self.solution)):
            self.solution[i] = self.solution[i] + self.velocity[i]
        return