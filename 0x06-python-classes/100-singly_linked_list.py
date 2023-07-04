#!/usr/bin/python3
"""This is a module to pass an advanced Task
Here we define a class of a node
This node is part of a singly linked list
"""


class Node:
    """This is a node class
    Attributes:
        size (int): size of square
    """
    def __init__(self, data, next_node=None):
        """init time for a new instance"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @property
    def next_node(self):
        return self.__next_node

    @data.setter
    def data(self, value):
        if (type(value) != int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @next_node.setter
    def next_node(self, value):
        if (type(value) != Node and value is not None):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """Class linked list"""
    def __init__(self):
        self.__head = None

    def __str__(self):
        """Display data when printing a linked list instance"""
        shlist = ""
        temp = self.__head
        while (temp is not None):
            shlist = shlist + str(temp.data) + '\n'
            temp = temp.next_node
            if (temp is None):
                shlist = shlist[:-1]
        return shlist

    def sorted_insert(self, value):
        """The most important method is this one"""
        new = None
        if self.__head is None:
            self.__head = Node(value, None)
        else:
            prev = None
            temp = self.__head
            while (temp is not None):
                if temp.data < value:
                    pass
                else:
                    new = Node(value, temp)
                    if prev is not None:
                        prev.next_node = new
                    else:
                        self.__head = new
                    break
                prev = temp
                temp = temp.next_node
            if new is None:
                new = Node(value, None)
                prev.next_node = new
