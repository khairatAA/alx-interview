#!/usr/bin/python3

"""
Pascal's Triangle
Create a function def pascal_triangle(n): that returns a list of lists
of integers representing the Pascal triangle of n:

Returns an empty list if n <= 0
You can assume n will be always an integer
"""


def pascal_triangle(n):
    """
    pascal_triangle: Pascal's Triangle Function
    n(args): Length of the list of m=be return
    """

    if n <= 0:
        return []

    arr = [[1]]

    for row in range(1, n):
        curr_row = [1]
        for col in range(1, row):
            val = arr[row - 1][col - 1] + arr[row - 1][col]
            curr_row.append(val)
        curr_row.append(1)
        arr.append(curr_row)

    return arr
