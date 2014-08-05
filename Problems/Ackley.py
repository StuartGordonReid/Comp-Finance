__author__ = 'Stuart Gordon Reid'
__email__ = 'stuartgordonreid@gmail.com'
__website__ = 'http://www.stuartreid.co.za'

"""
http://www-optima.amp.i.kyoto-u.ac.jp/member/student/hedar/Hedar_files/TestGO_files/Page295.htm
"""

from Problems.Problem import Problem


class Ackley(Problem):

    def __init__(self, dimension):
        super(Ackley, self).__init__(dimension)

    def evaluate(self, candidate):
        """
        LaTeX: f_{\textrm{Cigar}}(\textbf{x}) = x_0^2 + \sum_{i=1}^N x^2_i
        """
        if len(candidate) == self.dimension:
            value = 0
            #TODO: Finish this
            return value
        else:
            raise Exception("Error candidate solution != dimension")
        pass
