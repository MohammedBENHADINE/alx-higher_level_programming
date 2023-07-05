#!/usr/bin/python3
def magic_string(lis=[0]):
    lis[0] += 1
    return "BestSchool" + (", BestSchool" * (lis[0] - 1))
