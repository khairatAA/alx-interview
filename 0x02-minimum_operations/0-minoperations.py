#!/usr/bin/python3
"""
Minimum Operations
"""


def minOperations(n):
    """
    n a text file, there is a single character H. Your text editor
    can execute only two operations in this file: Copy All and Paste.
    Given a number n, write a method that calculates the fewest number
    of operations needed to result in exactly n H characters in the file.
    """
    if n < 2:
        return 0

    tracker = 0

    file_content = 1

    while file_content <= n:
        # if n % file_content == 0:
        file_content *= 2
        tracker += 1
        # else:
        #     return 0

    return tracker
