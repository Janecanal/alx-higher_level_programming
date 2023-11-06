#!/usr/bin/python3

"""writes a class that inherits from list"""


class MyList(list):

    """a function that prints list in ascending order"""
    def print_sorted(self):
        """prints sorted list"""
        print(sorted(self))
