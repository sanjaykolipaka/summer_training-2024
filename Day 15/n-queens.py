def isSafe(board, r, c, n):
    # Check the column
    for i in range(r):
        if board[i][c] == 1:
            return False

    # Check the upper right diagonal
    i, j = r, c
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    # Check the upper left diagonal
    i, j = r, c
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    return True

def queen(board, r, n):
    if r >= n:
        return True

    for c in range(n):
        if isSafe(board, r, c, n):
            board[r][c] = 1
            if queen(board, r + 1, n):
                return True
            board[r][c] = 0  # Backtrack

    return False

def solveNQueens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    if queen(board, 0, n):
        for row in board:
            print(row)
    else:
        print("No solution exists")

n = 19
solveNQueens(n)
