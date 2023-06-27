#!/usr/bin/python3
"""
Module 100-singly_linked_list
defines a node of a singly linked list
"""


class Node:
    """
    class Node definition

    Args:
        data (int): data of the node

    Functions:
        __init__(self, value)
        data(self)
        data(self, value)
    """
    def __init__(self, data=None, next_node=None):
        """
        initializes a Node

        Attributes:
            value (int): data of the node
            next_node (Node): next node
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """
        Getter

        Returns: data of a node
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Setter

        Args:
            value: to be set to data
        """
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """
        Getter

        Returns: the next node
        """
        return self.__next_node
    @next_node.setter
    def next_node(self, value):
        """
        Setter

        Args:
            value: to be set to next_node
        """
        if type(value) is not Node and value is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value

class SinglyLinkedList:
    def __init__(self):
        """
        Initializes a list
        """
        self.__head = None

    def __str__(self):
        """
        print the entire list in stdout
        """
        temp = self.__head
        result = ""
        while temp is not None:
            result += str(temp.data) + "\n"
            temp = temp.next_node
        return result

    def sorted_insert(self, value):
        """
        Inserts a new Node

        Args:
            value: data for the new node
        """
        new_node = Node(value)
        temp = self.__head
        if self.__head is None:
            self.__head = new_node
            return

        if new_node.data < temp.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return
        while temp.next_node is not None and temp.next_node.data < value:
            temp = temp.next_node
        new_node.next_node = temp.next_node
        temp.next_node = new_node
