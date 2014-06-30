__author__ = 'Stuart Gordon Reid'
__email__ = 'stuartgordonreid@gmail.com'
__website__ = 'http://www.stuartreid.co.za'

"""
This file contains an implementation of the Queue data structure which uses a Linked List
"""

from LinkedList import LinkedList


class Queue():
    """
    This code contains a Queue data-structure implementation based on the LinkedList class
    """

    type = "queue"
    list = None

    def __init__(self):
        self.list = LinkedList()
        pass

    def push(self, data):
        self.list.add_node(data)

    def pop(self):
        if self.list.size > 0:
            return self.list.remove_node(0)
        else:
            return None


if __name__ == "__main__":
    # Testing method
    my_queue = Queue()

    my_data = my_queue.pop()
    assert my_data is None
    print "Passed first test - pop"

    my_queue.push(45)
    assert my_queue.list.extract_data() == [45]
    print "Passed second test - push 1"

    my_queue.push(37)
    assert my_queue.list.extract_data() == [45, 37]
    print "Passed third test - push 2"

    my_queue.push("ABC")
    assert my_queue.list.extract_data() == [45, 37, "ABC"]
    print "Passed fourth test - push 3"

    my_data = my_queue.pop()
    assert my_data is 45
    print "Passed fifth test - pop"

    my_data = my_queue.pop()
    assert my_data is 37
    print "Passed sixth test - pop"

    my_data = my_queue.pop()
    assert my_data is "ABC"
    print "Passed seventh test - pop"