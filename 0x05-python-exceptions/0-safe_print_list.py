#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    idx = 0
    try:
        for item in my_list:
            if x > idx:
                print(item, end="")
                idx += 1
    except IndexError:
        pass
    print()
    return idx
