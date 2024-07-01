#return the number ways of solution
def solveNQueens(n):
        sol=[]
        board = [['.' for _ in range(n)] for _ in range(n)]
        nqueen(n, sol,board, 0)
        return len(sol)
def nqueen(n, sol,board, row):
        if row == n:
            sol.append([''.join(row) for row in board])
            return
        for j in range(n):
            if issafe(board, row, j, n):
                board[row][j] = 'Q'
                nqueen(n,sol, board, row + 1)
                board[row][j] = '.'  # backtracking

def issafe(board, row, col, n):
    for i in range(n):  # check row
        if board[row][i] == 'Q':
            return False
    for i in range(n):  # check col
        if board[i][col] == 'Q':
            return False
        # check NE
    i, j = row, col
    while i >=0 and j < n:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1

        # check SE
    i, j = row, col
    while i < n and j < n:
        if board[i][j] == 'Q':
            return False
        i += 1
        j += 1

        # NW
    i, j = row, col
    while i >= 0 and j >=0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

        # SW
    i, j = row, col
    while i < n and j >= 0:
        if board[i][j] == 'Q':
            return False
        i += 1
        j -= 1
        return True
n=int(input("enter the size"))
print(solveNQueens(n))