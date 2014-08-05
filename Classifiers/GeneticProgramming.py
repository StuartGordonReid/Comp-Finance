from Optimizers.Solution import Solution

__author__ = 'stuartreid'


class GeneticProgramming():
    """
    This class contains a generic Genetic Programming (GP) algorithm implementation. This algorithm evolves a set of
    Individuals which represent tree-based solutions to a particular problem (Function object)
    """

    def __init__(self, parameters=None):
        """
        This method initializes the Population of Individuals to be evolved using the Genetic Programming (GP)
        algorithm. It has a set of default parameters and strategies for the evolutionary operators
        :param parameters[0]: Population size
        :param parameters[1]: Crossover rate
        :param parameters[2]: Mutation rate
        :param parameters[3]: Selection strategy
        :param parameters[4]: Crossover strategy
        :param parameters[5]: Mutation strategy
        """

        if parameters is None:
            parameters = [50, 0.7, 0.3, "rank", "sexual", "brownian"]
            self.parameters = parameters

        self.population = []
        for i in range(self.parameters[0]):
            self.population.append(Individual())

    def selection(self):
        pass

    def crossover(self):
        pass

    def mutation(self):
        pass


class Individual(Solution):

    def __init__(self, solution):
        super(Individual, self).__init__(solution)