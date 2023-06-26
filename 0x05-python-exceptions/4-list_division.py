#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    res_list = []
    for idx in range(0, list_length):
        try:
            item = my_list_1[idx] / my_list_2[idx]
        except TypeError:
            print("wrong type")
            item = 0
        except ZeroDivisionError:
            print("division by 0")
            item = 0
        except IndexError:
            print("out of range")
            item = 0
        finally:
            res_list.append(item)
    return res_list
