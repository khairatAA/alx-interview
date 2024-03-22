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

    divisor = 2

    while n > 1:
        while n % divisor == 0:
            tracker += 2
            n //= divisor
        divisor += 1

    return tracker
