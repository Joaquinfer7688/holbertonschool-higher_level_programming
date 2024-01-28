#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for fila in matrix:
        for a in range(0, len(fila)):
            print("{:d}".format(a), end=" " if a != fila[-1] else "")
            print()
