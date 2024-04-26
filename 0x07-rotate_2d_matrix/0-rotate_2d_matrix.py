#!/usr/bin/python3

def rotate_2d_matrix(matrix):
    '''
    Given an n x n 2D matrix, rotate it 90 degrees clockwise.
    Args:
        matrix: List of list.
    Return:
        Nothing.
    '''
    n = len(matrix)

    for layer in range(n // 2):
        first = layer
        last = n - 1 - layer

        for i in range(first, last):
            offset = i - first
            top = matrix[first][i]

            # left -> top
            matrix[first][i] = matrix[last - offset][first]

            # bottom -> left
            matrix[last - offset][first] = matrix[last][last - offset]

            # right -> bottom
            matrix[last][last - offset] = matrix[i][last]

            # top -> right
            matrix[i][last] = top
