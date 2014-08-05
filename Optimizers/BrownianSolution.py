__author__ = 'Stuart Gordon Reid'
__email__ = 'stuartgordonreid@gmail.com'
__website__ = 'http://www.stuartreid.co.za'

"""
File description
"""

import random
from Optimizers.Solution import Solution
from Problems.Cigar import Cigar


class BrownianSolution(Solution):

    def __init__(self, solution, problem, parameters=None):
        """
        :param solution: the initial solution
        :param parameters: [0] num attempts, [1] variance
        """
        super(BrownianSolution, self).__init__(solution, problem)
        if parameters is None:
            self.parameters = [10, 0.001]

    def update_solution(self):
        # For number of tries, try create a better solution randomly
        for i in range(self.parameters[0]):
            brownian = self.deep_copy()
            dimension = random.randint(0, self.problem.dimension - 1)
            brownian.solution[dimension] *= random.uniform(-self.parameters[1], self.parameters[1])
            if brownian > self:
                self.solution = brownian.solution


def brownian_solution_test():
    problem = Cigar(50, 25, -25)
    vector = random.sample(xrange(problem.lower_bound, problem.upper_bound), problem.dimension)

    brownian_solution = BrownianSolution(vector, problem)
    print problem.evaluate(brownian_solution.solution)
    brownian_solution.update_solution()
    print problem.evaluate(brownian_solution.solution)
    brownian_solution.update_solution()
    print problem.evaluate(brownian_solution.solution)

if __name__ == "__main__":
    brownian_solution_test()