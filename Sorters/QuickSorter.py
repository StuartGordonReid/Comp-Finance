from Sorters.Sorter import Sorter

__author__ = 'stuartreid'

import random


class QuickSorter(Sorter):
    """
    This class contains the source code for a Python implementation of the Quick Sort algorithm. A similar approach
    can be found here: http://rosettacode.org/wiki/Sorting_algorithms/Quicksort#Python
    """
    def __init__(self, data, ordering="ascending"):
        super(QuickSorter, self).__init__(data, ordering)

    def sort(self):
        sorted_data = self.quick_sort(self.data)
        if self.ordering is "ascending":
            return sorted_data
        elif self.ordering is "descending":
            return sorted_data[::-1]

    def quick_sort(self, partition):
        """
        :param partition: the partition (section of the data) to be sorted
        :return: returns the partition in a sorted
        """
        less = []
        pivot_list = []
        more = []
        if len(partition) <= 1:
            return partition
        else:
            pivot = partition[0]
            for i in partition:
                if i < pivot:
                    less.append(i)
                elif i > pivot:
                    more.append(i)
                else:
                    pivot_list.append(i)
            less = self.quick_sort(less)
            more = self.quick_sort(more)
            return less + pivot_list + more


def test(length=100):
    random_data = random.sample(xrange(0, 100), length)
    sorter = QuickSorter(random_data)
    print "Unsorted: ", random_data
    sorted_data = sorter.sort()
    print "Sorted: ", sorted_data


if __name__ == "__main__":
    test(10)
