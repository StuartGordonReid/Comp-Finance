__author__ = 'stuartreid'


class Crossover():
    """
    Contains a generic implementation of a Crossover strategy. This class is overloaded by specific selection strategies
    which can be used by the Genetic Algorithm as well as the Genetic Programming algorithm (classifiers)
    """
    def __init__(self, selection_type="sexual"):
        if selection_type is "sexual":
            self.crossover = SexualCrossover()
        elif selection_type is "asexual":
            self.crossover = AsexualCrossover()

    def get_crossover(self):
        return self.crossover


class SexualCrossover():
    """

    """
    def __init__(self):
        pass


class AsexualCrossover():
    """

    """
    def __init__(self):
        pass
