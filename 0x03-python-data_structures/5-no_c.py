#!/usr/bin/python3
def no_c(my_string):
    length = len(my_string)
    if length > 0:
        new_str = ""
        for i in range(length):
            if (my_string[i] != "c") and my_string[i] != "C":
                new_str += my_string[i]
        return new_str
    return my_string
