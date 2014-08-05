__author__ = 'stuartreid'


class Mutation():
    """
    Contains a generic implementation of a Selection strategy. This class is overloaded by specific selection strategies
    which can be used by the Genetic Algorithm as well as the Genetic Programming algorithm (classifiers)
    """
    def __init__(self, selection_type="brownian"):
        if selection_type is "rank":
            self.mutator = BrownianMutation()

    def get_mutator(self):
        return self.mutator


class BrownianMutation():
    """

    """
    def __init__(self):
        pass
