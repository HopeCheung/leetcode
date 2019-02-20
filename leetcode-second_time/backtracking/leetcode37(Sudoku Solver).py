class Solution:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def solveSudoku(self, board):
        def is_valid(x, y, n):
            if n in board[x]:
                return False
            if n in [board[i][y] for i in range(len(board[0]))]:
                return False
            for i in range(x - x%3, x - x%3 + 3):
                for j in range(y - y%3, y - y%3 + 3):
                    if board[i][j] == n:
                        return False
            return True

        def find_empty():
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == ".":
                        return i, j
            return -1, -1
        
        def solve():
            x, y = find_empty()
            if x == -1 and y == -1:
                return True
            for n in "123456789":
                if is_valid(x, y, n):
                    board[x][y] = n
                    if solve():
                        return True
                    board[x][y] = "."
            return False
        solve()
        

            
            

