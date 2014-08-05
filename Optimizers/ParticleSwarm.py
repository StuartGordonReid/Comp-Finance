from Problems.Problem import Problem

__author__ = 'Stuart Gordon Reid'
__email__ = 'stuartgordonreid@gmail.com'
__website__ = 'http://www.stuartreid.co.za'

"""
File description
"""

import random

from Optimizers.Optimizer import Optimizer
from Optimizers.Solution import Solution
from Optimizers.BrownianSolution import BrownianSolution
from Collections.AbstractNode import AbstractNode
from Problems.Cigar import Cigar


class ParticleSwarm(Optimizer):
    """
    This class contains an implementation of a standard no-frills Particle Swarm Optimizer
    """

    def __init__(self, problem, parameters=None):
        """
        Initialization method for the Particle Swarm Optimizer
        :param problem: the problem being optimized
        :param parameters: 0 = Inertia, 1 = Cognitive Component (C1), 2 = Social Component (C2), 3 = Swarm Size
        4 = Use Brownian Particle True / False
        """
        assert isinstance(problem, Problem)
        #Don't ask me why, http://effbot.org/zone/default-values.htm
        if parameters is None:
            parameters = [0.729844, 1.496180, 1.496180, 50, True]
        super(ParticleSwarm, self).__init__(problem, parameters)

        #Create swarm
        self.swarm = []
        #Initialize each particle
        for i in range(parameters[3]):
            velocities = [0] * problem.dimension
            #ToDo: there are some issues with this Pythonic code sigh!
            random_solution = random.sample(xrange(problem.lower_bound, problem.upper_bound), problem.dimension)
            self.swarm.append(Particle(problem, random_solution, random_solution, velocities))

    def optimize(self, iterations=1000, stopping=True):
        #Initialize container variables for global best & fitness
        global_best = self.swarm[0]
        for i in range(1, iterations):
            #Get the global best particle in the swarm (best of personal bests)
            for particle in self.swarm:
                #Check the type of the problem min or max
                if particle > global_best:
                    global_best = particle

            #Update each particle in the swarm
            print "Fitness at ", i, " is ", "{0:.15f}".format(global_best.evaluate())
            for particle in self.swarm:
                if particle.solution != global_best.solution:
                    particle.update_velocity(global_best)
                    particle.update_solution()
                else:
                    if self.parameters[4]:
                        brownian_solution = BrownianSolution(particle.solution, self.problem)
                        brownian_solution.update_solution()
                        particle.solution = brownian_solution.solution
        return global_best


class Particle(Solution, AbstractNode):
    """
    This class is an implementation of the Particle used in a PSO. Particle updates consist of two steps, calculating
    the new velocities and updating them, then calculating the new position by adding the velocities to the position
    """

    def __init__(self, problem, solution, best_solution, velocity):
        """
        Overloaded solution object for the Particle Swarm Optimizer
        :type best_solution: object
        :param solution:
        :param velocity:
        :param best_solution:
        """
        self.velocity = velocity
        self.best_solution = best_solution
        #Updates the solution numpy array in super
        super(Particle, self).__init__(solution, problem)

    def update_velocity(self, global_best, parameters=None):
        """
        This method updates the Particles velocity w.r.t the global best and control parameters
        """
        global_best_solution = global_best.solution
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


def pso_test():
    problem = Cigar(300, 200, -200)
    pso = ParticleSwarm(problem)
    pso.optimize(100)


if __name__ == "__main__":
    pso_test()