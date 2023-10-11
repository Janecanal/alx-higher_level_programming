#!/usr/bin/python3

def _get_value(char):
    """
    Returns the roman value of a character
    None if its not a Roman Character
    """
    romans = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 100
    }
    char = char.upper()
    if char in romans:
        return romans[char]
    return None
