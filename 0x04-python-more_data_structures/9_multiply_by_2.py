#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = dict(a_dictionary)
    for x in list(new):
        new[x] = new[x] * 2
    return new
