from Sorters.Sorter import Sorter
import random

__author__ = 'stuartreid'


class HeapSorter(Sorter):
    """
    This class contains the source code for an implementation of the HeapSort algorithm.
    """
    def __init__(self, data, ordering="ascending"):
        super(HeapSorter, self).__init__(data, ordering)

    def sort(self):
        sorted_data = self.heap_sort(self.data)
        if self.ordering is "ascending":
            return sorted_data
        elif self.ordering is "descending":
            return sorted_data[::-1]

    def heap_sort(self, partition):
        # in pseudo-code, heapify only called once, so inline it here
        for start in range((len(partition) - 2) / 2, -1, -1):
            self.sift_down(partition, start, len(partition) - 1)

        for end in range(len(partition) - 1, 0, -1):
            partition[end], partition[0] = partition[0], partition[end]
            self.sift_down(partition, 0, end - 1)
        return partition

    @staticmethod
    def sift_down(partition, start, end):
        root = start
        while True:
            child = root * 2 + 1
            if child > end:
                break
            if child + 1 <= end and partition[child] < partition[child + 1]:
                child += 1
            if partition[root] < partition[child]:
                partition[root], partition[child] = partition[child], partition[root]
                root = child
            else:
                break


def test(length=100):
    random_data = random.sample(xrange(0, 100), length)
    sorter = HeapSorter(random_data)
    print "Unsorted: ", random_data
    sorted_data = sorter.sort()
    print "Sorted: ", sorted_data


if __name__ == "__main__":
    test(10)