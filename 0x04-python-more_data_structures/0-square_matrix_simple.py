#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared = list(map(lambda line: list(map(lambda c: c**2, line)), matrix))
    return squared
