#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if (len(my_list) == 0):
        return []
    else:
        res = []
        for i in range(0, len(my_list)):
            if (my_list[i] % 2):
                res.append(False)
            else:
                res.append(True)
        return res
