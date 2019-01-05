class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if len(board) == 0:
            return
        queue = []
        
        def fill(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != 'O':
                return
            queue.append((i, j))
            board[i][j] = 'D'
        
        def bfs(x, y):
            if board[x][y] == 'O':
                fill(x, y)
            while queue:
                curr = queue.pop()
                i, j = curr[0], curr[1]
                fill(i - 1, j)
                fill(i + 1, j)
                fill(i, j - 1)
                fill(i, j + 1)
        
        m, n = len(board), len(board[0])
        for i in range(m):
            bfs(i, 0)
            bfs(i, n-1)
        for j in range(n):
            bfs(0, j)
            bfs(m-1, j)
            
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'D':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
            
        
            
        