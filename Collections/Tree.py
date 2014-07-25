__author__ = 'Stuart Gordon Reid'
__email__ = 'stuartgordonreid@gmail.com'
__website__ = 'http://www.stuartreid.co.za'

"""
This class contains the implementation for a binary search tree (BST)
"""

from AbstractNode import AbstractNode
import random


class Tree():
    """
    This class contains the implementation for a binary search tree (BST)
    """

    type = "list"
    head = None
    size = 0

    def __init__(self):
        self.head = None
        self.size = 0
        pass

    def add(self, data):
        #Tree is empty
        if self.size == 0:
            self.head = AbstractNode(data)
            self.size += 1
        else:
            curr_node = self.head
            #assert isinstance(curr_node, AbstractNode)
            while True:
                #Right branch of current
                if data > curr_node.get_data():
                    if curr_node.get_right() is None:
                        #Insert new node with data as the right child
                        curr_node.set_right(AbstractNode(data))
                        self.size += 1
                        break
                    else:
                        curr_node = curr_node.get_right()
                #Left branch of current
                elif data < curr_node.get_data():
                    if curr_node.get_left() is None:
                        #Insert new node with data as the left child
                        curr_node.set_left(AbstractNode(data))
                        self.size += 1
                        break
                    else:
                        curr_node = curr_node.get_left()
                else:
                    curr_node.increment()
                    self.size += 1
                    break

    def remove(self, data):
        #TODO: Finish this method
        #Tree is empty
        if self.size == 0:
            return
        elif data == self.head.get_data():
            self.head = None
        else:
            pass

    def __remove__(self, curr_node, data):
        pass

    def print_tree(self):
        self.__print_tree__(self.head, "")

    def __print_tree__(self, node, prefix):
        if node is not None:
            count = node.get_count()
            if count == 1:
                print prefix, "+-", node.get_data()
            else:
                print prefix, "+-", node.get_data(), "x", count
            self.__print_tree__(node.get_left(), prefix + " | ")
            self.__print_tree__(node.get_right(), prefix + " | ")


if __name__ == "__main__":
    my_tree = Tree()
    for i in range(15):
        my_tree.add(random.randint(0, 15))
    my_tree.print_tree()
