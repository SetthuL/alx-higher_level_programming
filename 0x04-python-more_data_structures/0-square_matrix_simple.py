#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()

    for sl in range(len(matrix)):
        new_matrix[sl] = list(map(lambda x: x**2, matrix[sl]))
    return (new_matrix)
