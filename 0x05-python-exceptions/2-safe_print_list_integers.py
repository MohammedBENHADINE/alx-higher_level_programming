#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    out = 0
    for item in range(0, x):
        try:
            print("{:d}".format(my_list[item]), end="")
            out += 1
        except (ValueError, TypeError):
            pass
    print()
    return out
