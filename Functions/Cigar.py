__author__ = 'Stuart Gordon Reid'
__email__ = 'stuartgordonreid@gmail.com'
__website__ = 'http://www.stuartreid.co.za'

"""
File description
"""

from Functions.Function import Function


class Cigar(Function):

    def __init__(self, dimension):
        super(Cigar, self).__init__(dimension)

    def evaluate(self, candidate):
        """
        LaTeX: f_{\textrm{Cigar}}(\textbf{x}) = x_0^2 + \sum_{i=1}^N x^2_i
        """
        if len(candidate) == self.dimension:
            value = 0
            for i in range(0, self.dimension):
                value += candidate[i] ** 2
            return value
        else:
            raise Exception("Error candidate solution != dimension")
        pass
