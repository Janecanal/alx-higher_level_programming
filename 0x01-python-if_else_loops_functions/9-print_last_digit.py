#!/usr/bin/python3

# print_last_digit: function that print last digit of any number
# num: arguments that hold pass variable or value
# lastd: hold last digit of passed argument
# Return: Last digit

def print_last_digit(num):
    if num < 0:
        lastd = (-1 * num) % 10

    else:
        lastd = num % 10
    print('{}'.format(lastd), end='')

    return lastd
