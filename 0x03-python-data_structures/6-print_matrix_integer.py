#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i in row:
            if (row[len(row) - 1] == i):
                print("{:d}".format(i), end='')
            else:
                print("{:d}".format(i), end=' ')
        print("")
