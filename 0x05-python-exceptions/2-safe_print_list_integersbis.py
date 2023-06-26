#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    idx = 0
    try:
        for item in my_list:
            if x > idx:
                print("{:d}".format(item), end="")
                idx += 1
    except (ValueError, TypeError):
        pass
    print()
    return idx
