__author__ = 'Stuart Gordon Reid'
__email__ = 'stuartgordonreid@gmail.com'
__website__ = 'http://www.stuartreid.co.za'

"""
File description
"""

from Problems.Problem import Problem


class Cigar(Problem):

    def __init__(self, dimension, upper_bound, lower_bound, optimization="min"):
        super(Cigar, self).__init__(dimension, upper_bound, lower_bound, optimization)

    def evaluate(self, candidate):
        """
        LaTeX: f_{\textrm{Cigar}}(\textbf{x}) = x_0^2 + \sum_{i=1}^N x^2_i
        """
        value = 0
        for i in xrange(0, self.dimension):
            value += candidate[i] ** 2
            #ToDo: move this out into the Abstract base class and force call
            if candidate[i] > self.upper_bound or candidate < self.lower_bound:
                if self.optimization is "min":
                    value = float("+inf")
                    break
                elif self.optimization is "max":
                    value = float("-inf")
                    break
        return value
