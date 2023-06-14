#!/usr/bin/python3
def uniq_add(my_list=[]):
    return sum(list(map(lambda x: x, set(my_list))))
