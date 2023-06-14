#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for x in sorted(list(a_dictionary)):
        print("{}: {}".format(x, a_dictionary.get(x)))
