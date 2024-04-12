#!/usr/bin/python3
import sys


def is_safe(board, row, col, N):
    # Check if there is a queen in the same column or diagonals
    for i in range(row):
        if board[i] == col or \
            board[i] - i == col - row or \
                board[i] + i == col + row:
            return False
    return True


def solve_n_queens_util(board, row, N, solutions):
    if row == N:
        solutions.append(board[:])
        return

    for col in range(N):
        if is_safe(board, row, col, N):
            board[row] = col
            solve_n_queens_util(board, row + 1, N, solutions)


def nQueens():
    if len(sys.argv) != 2:
        print('Usage: nqueens N\n', file=sys.stderr)
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print('N must be a number\n', file=sys.stderr)
        sys.exit(1)

    if N < 4:
        print('N must be at least 4\n', file=sys.stderr)
        sys.exit(1)

    solutions = []
    solve_n_queens_util([-1] * N, 0, N, solutions)

    for sol in solutions:
        print([[i, col] for i, col in enumerate(sol)])

    sys.exit(0)


if __name__ == "__main__":
    nQueens()
