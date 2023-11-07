#!/usr/bin/python3
"""a function that returns true,"""
"""if object is an instance of a class"""


def inherits_from(obj, a_class):
    """checks if the obj is an instance"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        """checks bool"""
        return True
    return False
