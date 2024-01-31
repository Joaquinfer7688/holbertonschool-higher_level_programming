#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newmatrix = []

    for a in range(len(matrix[a])):
        for b in range(len(matrix[b])):
            newmatrix[a][b] = matrix[a][b] ** 2

    return newmatrix
