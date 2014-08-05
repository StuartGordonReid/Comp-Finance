__author__ = 'Stuart Gordon Reid'
__email__ = 'stuartgordonreid@gmail.com'
__website__ = 'http://www.stuartreid.co.za'

"""
File description
"""


class Solution(object):
    solution = []

    def __init__(self, solution, problem):
        """
        Abstract initialization method for a solution to some optimization function
        :param solution: a numpy array (much faster than lists)
        """
        self.solution = solution
        self.problem = problem
        return

    def __len__(self):
        """
        Overload of the len operator for the Solution class
        :rtype : Sized?
        """
        return len(self.solution)

    def update(self, solution):
        """
        This method is used for updating a solution
        """
        self.solution = solution

    def get(self):
        """
        This method is used to retrieve the numpy array for direct manipulation
        """
        return self.solution

    def evaluate(self):
        return self.problem.evaluate(self.solution)

    def __gt__(self, other):
        assert isinstance(other, Solution)
        if self.problem.optimization is "min":
            return self.evaluate() < other.evaluate()
        elif self.problem.optimization is "max":
            return self.evaluate() > other.evaluate()

    def deep_copy(self):
        copy = Solution(None, self.problem)
        copy.solution = []
        for i in range(len(self.solution)):
            copy.solution.append(self.solution[i])
        return copy

