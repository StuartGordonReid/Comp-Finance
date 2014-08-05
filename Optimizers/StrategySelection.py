__author__ = 'Stuart Gordon Reid'
__email__ = 'stuartgordonreid@gmail.com'
__website__ = 'http://www.stuartreid.co.za'

"""
File description
"""


class Selection():
    """
    Contains a generic implementation of a Selection strategy. This class is overloaded by specific selection strategies
    which can be used by the Genetic Algorithm as well as the Genetic Programming algorithm (classifiers)
    """
    def __init__(self, selection_type="rank"):
        if selection_type is "rank":
            self.selector = RankSelection()
        if selection_type is "random":
            self.selector = RandomSelection()

    def get_selector(self):
        return self.selector


class RankSelection():
    """

    """
    def __init__(self):
        pass


class RandomSelection():
    """

    """
    def __init__(self):
        pass
