class Solution:
    def solveNQueens(self, n: 'int') -> 'List[List[str]]':
        if n == 0:
            return []
        board = ["." * n] * n
        res = []
        def is_valid(x, y, board, n):
            if "Q" in board[x]:
                return False
            if "Q" in [board[i][y] for i in range(n)]:
                return False
            i, j = x, y
            while i < n and j < n:
                if board[i][j] == "Q":
                    return False
                i, j = i + 1, j + 1
            i, j = x, y
            while i < n and j >= 0:
                if board[i][j] == "Q":
                    return False
                i, j = i + 1, j - 1
            i, j = x, y
            while i >= 0 and j < n:
                if board[i][j] == "Q":
                    return False
                i, j = i - 1, j + 1
            i, j = x, y
            while i >= 0 and j >= 0:
                if board[i][j] == "Q":
                    return False
                i, j = i - 1, j - 1
            return True
        
        def solve(row, n):
            if row == n:
                res.append(board[:])
                return
            for col in range(n):
                if is_valid(row, col, board, n):
                    board[row] = board[row][0:col] + 'Q' + board[row][col+1:]
                    solve(row+1, n)
                    board[row] = board[row][0:col] + '.' + board[row][col+1:]
        solve(0, n)
        return res
                        
        