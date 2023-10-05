#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div

if __name__ == '__main__':
    """
    Handles basic operations

    Performs basic operations like addition, substraction,
    multiplication and division between two numbers.

    The program will execute an operation between two numbers
    selected by the operator sent to the program.
    """
    l_av = len(argv) - 1
