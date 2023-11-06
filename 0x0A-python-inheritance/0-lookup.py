#!/usr/bin/python3

def lookup(obj):

    """lookup is a function that returns the available attributes and methods of an object"""
    return list(dir(obj))
