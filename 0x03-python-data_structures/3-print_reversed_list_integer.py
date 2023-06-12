#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    n = len(my_list)
    for i in range(0, n):
        print("{:d}".format(my_list[n - i - 1]))
