#!/usr/bin/python3
""" Node and Singly linked list class"""


class Node:
    """
    Node class represents a node in a singly linked list.

    Attributes:
        __data (int): The data stored in the node.
        __next_node (Node): The reference to the next node in the list.
    """
    def __init__(self, data, next_node=None):
        """Initializes the data.
        Args:
            data (int): data to store
            next_node (Node object): reference to next_node
        """
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        self.__data = data
        if not isinstance(next_node, Node) and next_node is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = next_node

    @property
    def data(self):
        """getter __data private instance attribute"""
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """getter __position private instance attribute"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


class SinglyLinkedList:
    """Defines a singly linked list"""
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a new Node into the correct sorted position in the list"""
        new_node = Node(value)
        if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return
        temp = self.__head
        while temp.next_node is not None and temp.next_node.data < value:
            temp = temp.next_node
        if new_node is not None:
            new_node.next_node = temp.next_node
        temp.next_node = new_node

    def __str__(self):
        result = []
        current = self.__head
        while current:
            result.append(str(current.data))
            current = current.next_node
        return '\n'.join(result)
