from Sorters.Sorter import Sorter

__author__ = 'Stuart Gordon Reid'
__email__ = 'stuartgordonreid@gmail.com'
__website__ = 'http://www.stuartreid.co.za'

"""
File description
"""

import random

class BitonicSorter(Sorter):
    """
    This class contains an implementation of the Bitonic Sorting algorithm for lists of data which are bitonic. A
    sequence is bitonic if it monotonically increases and then monotonically decreases
    """

    def __init__(self, data, ordering="ascending"):
        """
        Initialization method for the Bitonic Sorter
        :param data: The list of data to be sorted
        :param ordering: The ordering to sort the data into
        """
        super(BitonicSorter, self).__init__(data, ordering)

    def sort(self):
        """
        Calls the bitonic sorting method
        :rtype : sorted list
        """
        if self.ordering is "ascending":
            return self.bitonic_sort(True, self.data)
        elif self.ordering is "descending":
            return self.bitonic_sort(False, self.data)

    def bitonic_sort(self, up, partition):
        """
        Recursive function for sorting the list
        :param up: True or False, depends on the direction we are going through the list
        :param partition: a partition of the original list to be sorted
        :return: 
        """
        # print "sorting: ", partition
        if len(partition) <= 1:
            return partition
        else:
            first = self.bitonic_sort(True, partition[:len(partition) / 2])
            second = self.bitonic_sort(False, partition[len(partition) / 2:])
            return self.bitonic_merge(up, first + second)

    def bitonic_merge(self, up, partition):
        """
        Recursive function to merge sorted partitions in the list
        :param up: True or False, depends on the direction we are going through the list
        :param partition: a partition of the original list which has been sorted
        :return:
        """
        # assume input x is bitonic, and sorted list is returned
        if len(partition) == 1:
            return partition
        else:
            self.bitonic_compare(up, partition)
            first = self.bitonic_merge(up, partition[:len(partition) / 2])
            second = self.bitonic_merge(up, partition[len(partition) / 2:])
            return first + second

    @staticmethod
    def bitonic_compare(up, partition):
        """
        A comparator method for individuals in the list used for swapping elements
        """
        dist = len(partition) / 2
        for i in range(dist):
            if (partition[i] > partition[i + dist]) == up:
                partition[i], partition[i + dist] = partition[i + dist], partition[i]
                #swap


def bitonic_test():
    #data = [10, 30, 11, 20, 4, 330, 21, 110]
    #data = [10, 30, 40, 20, 4, 1, 21, 110]
    #data = [10, 30, 40, 60, 55, 45, 35, 89, 92, 99, 101, 123, 115, 111, 100, 99]
    data = random.sample(xrange(0, 100), 64)
    print "Unsorted: ", data
    sorter = BitonicSorter(data)
    sorted_data = sorter.sort()
    print "Sorted: ", sorted_data


if __name__ == "__main__":
    bitonic_test()