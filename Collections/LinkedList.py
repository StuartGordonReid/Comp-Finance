__author__ = 'Stuart Gordon Reid'
__email__ = 'stuartgordonreid@gmail.com'
__website__ = 'http://www.stuartreid.co.za'

"""
This file contains an implementation of a doubly-linked Linked List
"""

from AbstractNode import AbstractNode


class LinkedList():
    """
    This class contains an implementation of the LinkedList object which is designed to work with the AbstractNode
    object. AbstractNode can be overloaded or used as it currently stands
    """
    type = "list"
    head = None
    tail = None
    size = 0

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        pass

    def add_node(self, data, index=0):
        """
        This method adds a new node either at the end or at the specified index counting from the front of the list
        :param data:
        :param index:
        """
        #List is empty
        if self.size == 0:
            self.head = AbstractNode(data)
            self.tail = self.head
            self.head.set_prev(self.tail)
            self.size += 1

        #Default parameters (end of list)
        elif index == 0:
            new_node = AbstractNode(data)
            self.tail.set_next(new_node)
            old_tail = self.tail
            self.tail = self.tail.get_next()
            self.tail.set_prev(old_tail)
            self.size += 1

        #Non-default parameters (anywhere in list)
        elif 0 < index < self.size:
            node = self.head
            for i in range(index):
                node = node.get_next()
            #Add the new node into the list
            prev_node = node.get_prev()
            new_node = AbstractNode(data)
            prev_node.set_next(new_node)
            new_node.set_prev(prev_node)
            #Link the new node to the old node
            prev_node = prev_node.get_next()
            prev_node.set_next(node)
            node.set_prev(prev_node)
            self.size += 1

        #Error if no case satisfied
        else:
            print("Invalid argument: add ", index)

    def remove_node(self, index=-1):
        """
        This method either removed a node from the end of the list or at the specified index counting from
        the front of the list
        :param index:
        """
        return_data = None
        #The list is empty
        if self.size == 0:
            return return_data

        #Delete the last element
        elif index == -1:
            return_data = self.tail.get_data()
            self.tail = self.tail.get_prev()
            self.tail.set_next(None)
            self.size -= 1
            return return_data

        #Delete the first element
        elif index == 0:
            return_data = self.head.get_data()
            self.head = self.head.get_next()
            self.size -= 1
            return return_data

        #Delete a valid element
        elif 0 <= index < (self.size - 1):
            node = self.head
            for i in range(index):
                node = node.get_next()
            return_data = node.get_data()

            #Get the prev node
            prev_node = node.get_prev()
            prev_node.set_next(node.get_next())
            next_node = node.get_next()
            next_node.set_prev(prev_node)
            self.size -= 1
            return return_data

        #Error if no case satisfied
        else:
            print("Invalid argument: remove ", index)
            return None

    def print_list(self):
        list_output = "Size = " + str(self.size) + " {"
        node = self.head
        while node is not None:
            list_output += str(node.get_data()) + ", "
            node = node.get_next()
        print list_output + "}"

    def load_data(self, data):
        for datum in data:
            self.add_node(datum)

    def extract_data(self):
        data = []
        node = self.head
        for i in range(self.size):
            data.append(node.get_data())
            node = node.get_next()
        return data


if __name__ == "__main__":
    # Testing method
    my_list = LinkedList()
    my_list.load_data([56, 45, 23, 89, 74])

    my_list.remove_node()
    assert my_list.extract_data() == [56, 45, 23, 89]
    print "Passed first test - pop"

    my_list.add_node(99)
    assert my_list.extract_data() == [56, 45, 23, 89, 99]
    print "Passed second test - push"

    my_list.remove_node(3)
    assert my_list.extract_data() == [56, 45, 23, 99]
    print "Passed third test - pop x"

    my_list.add_node(87, 2)
    assert my_list.extract_data() == [56, 45, 87, 23, 99]
    print "Passed fourth test - push x"
